import os
import time
import tarfile
from pathlib import Path
from pic_to_plan_v2.settings import ROOT_DIR, PYTHON2_PATH
import math

# like in ramirez implementation
# coefficient for likelihood
beta = 1

def call_plan_rec(instance_number, return_array, detailed_pr_vals_array, goal_strings):
    t0 = time.time()
    obs_trace_file = open(Path(ROOT_DIR, "pddl", "plan_rec_instances", "pr_instance_" + str(instance_number), "obs.dat"))
    obs_trace_string = "".join(obs_trace_file.readlines())
    obs_trace_file.close()

    max_prob = -1

    #needed to fill up the multiprocess return array
    i = instance_number * 3 * len(goal_strings)

    for goal in goal_strings:
        for c, condition in enumerate(["obs_sat", "obs_not_sat"]):
            cmd_string = os.path.join(ROOT_DIR, 'external', 'downward',
                              'fast-downward.py') + \
                              ' --plan-file ' + os.path.join(ROOT_DIR, "pddl", "plan_rec_instances", "pr_instance_" + str(instance_number),  "sas_plan") + ' ' + \
                              os.path.join(ROOT_DIR, "pddl", "plan_rec_instances", "pr_instance_" + str(instance_number), "plan_rec_domain.pddl") + ' ' + \
                              os.path.join(ROOT_DIR, "pddl", "plan_rec_instances", "pr_instance_" + str(instance_number), "plan_rec_instance_"+ goal + '_' + condition + '.pddl') + \
                              ' --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea], verbosity=silent)" > /dev/null 2>&1'
                              # > /dev/null 2>&1 is non system independent. prevents output to console
            print("FAST DOWNWARD:", goal, condition, obs_trace_string)
            os.system(cmd_string)
            if os.path.isfile(os.path.join(ROOT_DIR, "pddl", "plan_rec_instances", "pr_instance_" + str(instance_number),  "sas_plan")):
                plan_file = open(os.path.join(ROOT_DIR, "pddl", "plan_rec_instances", "pr_instance_" + str(instance_number),  "sas_plan"))
                plan_stings = plan_file.readlines()
                # e.g.: "; cost = 9 (unit cost)"
                cost = int(plan_stings[-1].split()[3])
                print("CALL PLAN REC DONE:", goal, condition, "obs:", obs_trace_string, cost)
            else: # no plan found --> no sas_plan file in folder
                cost = math.inf
                print("CALL PLAN REC DONE:", goal, condition, "obs:", obs_trace_string, "NO PLAN FOUND")

            detailed_pr_vals_array[i] = cost
            i += 1

            #when both obs_sat and obs_not_sat costs are known calculate P(O|G)
            if c == 1:
                # P(O|G) / P( \neg O | G) = exp { -beta Delta(G,O) }
                # Delta(G,O) = cost(G,O) - cost(G,\neg O)
                print("cost diff from", detailed_pr_vals_array[i - 2], detailed_pr_vals_array[i - 1])

                if(detailed_pr_vals_array[i - 2] == math.inf and detailed_pr_vals_array[i - 1] == math.inf):
                    detailed_pr_vals_array[i] = 0.5
                elif(detailed_pr_vals_array[i - 2] == math.inf):
                    detailed_pr_vals_array[i] = 0.0
                elif(detailed_pr_vals_array[i - 1] == math.inf):
                    detailed_pr_vals_array[i] = 1.0
                else:
                    likelihood_ratio = math.exp(-beta * (detailed_pr_vals_array[i - 2] - detailed_pr_vals_array[i - 1]))
                    # P(O|G) =  exp { -beta Delta(G,O) } / 1 + exp { -beta Delta(G,O) }
                    detailed_pr_vals_array[i] = likelihood_ratio / (1.0 + likelihood_ratio)
                print(detailed_pr_vals_array[i])
                max_prob = max(max_prob, detailed_pr_vals_array[i])
                i += 1

    t1 = time.time()
    duration = t1 - t0
    print("duration", duration)
    return_array[instance_number] = max_prob

def call_plan_rec_ramirez(instance_number, return_array, detailed_pr_vals_array):
    t0 = time.time()
    obs_trace_dir = os.path.dirname(os.path.realpath(__file__))
    print("Obs trace dir", obs_trace_dir)
    #location outside of project
    # os.chdir("/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/")
    #location within project
    os.chdir(str(Path(ROOT_DIR, "external/prob_plan_recognition_"+str(instance_number))))

    #os.system("python2 ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G \
    #    -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2")

    ###example call
    #os.execvp("/usr/bin/python", ["/usr/bin/python" ,"/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py",  "-G", \
    #    "-e", "/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2"])

    #works, but replaces process, s.t. the whole program terminates when this call is terminated
    #os.execvp("/usr/bin/python", ["/usr/bin/python" ,"/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py",  "-G", \
    #    "-e", "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/sample.tar.bz2"])

    #call outside of this project
    # #working call to pr
    # os.system("/usr/bin/python /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G \
    #         -e /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/sample.tar.bz2")

    os.system(PYTHON2_PATH +" " + str(Path(ROOT_DIR, "external/prob_plan_recognition_"+str(instance_number)+"/prob_PR.py")) +" -G  \
             -e " + str(Path(ROOT_DIR, "pddl/plan_rec_instances_ramirez/pr_instance_"+str(instance_number)+".tar.bz2")))

    results = tarfile.open(str(Path(ROOT_DIR, "external/prob_plan_recognition_"+str(instance_number)+"/results.tar.bz2")), "r:bz2")
    report = results.extractfile("report.txt")
    max_prob = 0
    no_goals = 0
    for l in report:
        l = str(l).split("=")
        l0 = l[0]
        if "Hyp_Prob_O" in l0:
            l1 = l[1].strip("\\n'")
            l1_float = float(l1)
            max_prob = max(max_prob, l1_float)
        if "Hyp_Atoms" in l0:
            no_goals += 1
    print("max prob", max_prob)

    #get detailed pr values
    report = results.extractfile("report.txt")
    i = instance_number * 3 * no_goals
    for l in report:
        l = str(l).split("=")
        l0 = l[0]
        if "Hyp_Cost_O" in l0:
            l1 = l[1].strip("\\n'")
            l1_float = float(l1)
            detailed_pr_vals_array[i] = l1_float
            i += 1
        if "Hyp_Cost_Not_O" in l0:
            l1 = l[1].strip("\\n'")
            l1_float = float(l1)
            detailed_pr_vals_array[i] = l1_float
            i += 1
        if "Hyp_Prob_O" in l0:
            l1 = l[1].strip("\\n'")
            l1_float = float(l1)
            detailed_pr_vals_array[i] = l1_float
            i += 1

    os.chdir(obs_trace_dir)
    t1 = time.time()
    duration = t1 - t0
    print("duration", duration)

    return_array[instance_number] = max_prob
    #Terminal call:
    #python ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2

# In /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/ :
# python ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2
# where in the planners.py I wrapped the FastDownward planner in lama-first mode for use by the prob-plan-rec script. \
#  In hypothesis.py or somewhere like this I changed call to LAMA to a call to FastDownward_LAMA. When not specifying a planner,
#  the FD planner is used. This is good, since the FD planner is also the standard planner for other planning calls in this
#  project.
# -G: greedy
# -e specify experiment file, must be compressed and contain the structure like in /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test
#  In that file, hyps is the goal set, obs is the observation trace, real_hyp is ground truth and won't be available when
#  running online.
#  A call to this delivers a results tar file, where the report.txt tells you which hypothesis (i.e., goal) is the most likely.
#  More interestingly, the hyp costs are to be considered, to compare the goals among each other. Don't forget, that for each
#  hypothesis, there is one modified planning problem incorporating the observation, and one avoiding the observed actions.