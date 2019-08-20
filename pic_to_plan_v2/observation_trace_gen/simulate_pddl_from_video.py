import pickle
import pic_to_plan_v2.observation_trace_gen.parsed_proplem as parsed_problem_mod
import pic_to_plan_v2.observation_trace_gen.video_annotation as video_annotation_mod
import os
import re
import time
from treelib import Node, Tree
import copy
import cProfile
import pstats
from pyprof2calltree import convert, visualize

def build_tree():
    t0 = time.time()
    t_start = time.time()

    #compile re for later use
    re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)")

    my_parsed_problem = parsed_problem_mod.ParsedPDDLProblem("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl", \
                                                                "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects.pddl")
    # dict from bounding boxes to parsed_problem_objects_dict.keys()
    bb_to_pddl_obj_dict = {'plastic_bag': ['plastic_bag1'], 'plastic_paper_bag': ['plastic_paper_bag1'], 'g_drawer': ['g_drawer1'],
         'sponge': ['sponge1'], 'drawer': ['drawer1', 'drawer2'], 'cuttingboard': ['cuttingboard1'], 'end': ['end1'],
         'bowl': ['bowl1'], 'r_hand': ['r_hand'], 'bread': ['bread1', 'bread2', 'bread3'], 'knife': ['knife1'], 'plate': ['plate1'],
         'cupboard': ['cupboard1'], 'peel': ['peel1'], 'fridge': ['fridge1'], 'cucumber': ['cucumber1'], 'sink': ['sink1'],
         'peeler': ['peeler1'], 'spice': ['spice1'], 'faucet': ['faucet1'], 'spice_holder': ['spice_holder1'],
         'towel': ['towel1'], 'counter': ['counter1'], 'spice_shaker': ['spice_shaker1'], 'l_hand': ['l_hand'],
         'g_drawer1': ['g_drawer11']}

    video_annotation = video_annotation_mod.VideoAnnotation(
            '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/Videos/', \
            '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/', \
            bb_to_pddl_obj_dict)

    session_name = "s13-d25"
    print(session_name)
    touch_events = pickle.load( open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/overlap_detections/touch_events_"+session_name+".p", "rb" ) )
    possible_actions_session = pickle.load( open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_"+session_name+".p", "rb" ) )

    #lama2011: /home/mk/Planning/fastdownwardplanner/fast-downward.py  --alias seq-sat-lama-2011 /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl
    # cmd = '/home/mk/Planning/fastdownwardplanner/fast-downward.py --validate /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl --search "astar(lmcut())" > fast_downward_out.txt'

    #get current state from parsed problem
    current_state_FD = my_parsed_problem.parsed_problem_FD.init
    current_state_set = set()
    for atom in current_state_FD:
        if atom.predicate != "=" and my_parsed_problem.onto[atom.predicate] is None: #TODO only add non-static atoms (static atoms defined in domain need to be checked, too?)
            s = "("+ str(atom.predicate) + " " + " ".join(atom.args) + ")"
            current_state_set.add(s)
            #print(s)
    current_state_string = " ".join(sorted(current_state_set))

    #put init state at root of tree
    #https://treelib.readthedocs.io/en/latest/
    tree = Tree()
    tree.create_node(str(current_state_string), 0, data=[current_state_set, ""]) #in the root there was no previous action
    open_state_set = [0]  #put the initial state as first element into the open state set
    state_string_to_node_id_dict = dict()
    state_string_to_node_id_dict[str(current_state_string)] = 0

    ###TODO the paragraph below is probably duplicate. it is done in the loop anyway
    template_instance = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects-insert-init.pddl", "r")
    template_instance_string = "".join(template_instance.readlines())
    parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
    f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl", "w")
    f.write(parsed_template_instance_string)
    f.close()

    tot_os_cmd_time = 0

    tree_id_counter = 1
    tree.show()
    for timestep in possible_actions_session:
        frame_no = timestep[0]
        open_state_set_for_timestep = []
        for s in open_state_set:
            current_plan_path_string = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plans/current_sas_plan_try_"
            try_action_strings = []
            for i, try_action in enumerate(timestep[1]):
                try_action_string = "(" + " ".join(try_action) + ")"    #create the plan for the action to try
                try_action_strings.append(try_action_string)
                f = open(current_plan_path_string+str(i), "w")
                f.write(try_action_string + "\n;cost = 1 (unit cost)")
                f.close()
            current_state_set = tree[s].data[0]
            current_state_string = " ".join(current_state_set)

            template_instance = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects-insert-init.pddl", \
                    "r")
            template_instance_string = "".join(template_instance.readlines())
            parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
            f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl", "w")
            f.write(parsed_template_instance_string)
            f.close()

            cmd = '/home/mk/Planning/VAL/validate -v /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl \
                    /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl ' \
                    + " ".join([current_plan_path_string+str(i) for i in range(len(timestep[1]))]) + \
                    ' > /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt'
            #cmd = '/home/mk/Planning/VAL/validate -v  /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/current-state-take-put-instance-no-handempty.pddl /home/mk/PycharmProjects/pic-to-plan/val_exp/open_sas_plan > plan_val_output.txt' #check for unsatisfied precondition --> action not applicable in current state
            t_os_start = time.time()
            os.system(cmd)
            t_os_end = time.time()
            tot_os_cmd_time += t_os_end - t_os_start

            plan_val_output = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt", "r")
            plan_val_output_joined = "".join(plan_val_output.readlines())
            #print(plan_val_output_joined)
            new_state_sets = []
            plan_val_output = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt", "r") #TODO superfluous open, but readlines changes the iterator...
            for line in plan_val_output:
                if "Checking plan" in line:
                    new_state_sets.append(copy.deepcopy(current_state_set))
                elif "Deleting" in line:
                    m = re_compiled.search(line)
                    atom_to_delete = m.group(0)
                    #print("DEL", atom_to_delete)
                    if atom_to_delete in new_state_sets[-1]:
                        new_state_sets[-1].remove(atom_to_delete)
                elif "Adding" in line:
                    m = re_compiled.search(line)
                    atom_to_add = m.group(0)
                    #print("ADD", atom_to_add)
                    if atom_to_add not in new_state_sets[-1]:
                        new_state_sets[-1].add(atom_to_add)

            sorted_new_state_strings = [" ".join(sorted(new_s)) for new_s in new_state_sets]
            for i, sorted_new_state_string in enumerate(sorted_new_state_strings):
                if sorted_new_state_string not in state_string_to_node_id_dict.keys():
                    tree.create_node(sorted_new_state_string, tree_id_counter, data=[new_state_sets[i], try_action_strings[i]], parent=tree[s].identifier) #in the root there was no previous action
                    open_state_set_for_timestep.append(tree_id_counter)
                    state_string_to_node_id_dict[sorted_new_state_string] = tree_id_counter
                    tree_id_counter += 1

            t1 = time.time()

            if t1-t0 > 30:
                t0 = t1
                tree.show()
                print(frame_no, tree_id_counter)

        open_state_set.extend(open_state_set_for_timestep)

    tree.show()
    t_stop = time.time()
    processing_time = t_stop - t_start
    print("FINISHED", "Frame no:", frame_no, "Node count:", tree_id_counter, "Tree depth:", tree.depth())
    print("Processing time:", processing_time, "Video length:", frame_no/30.0, "Realtime factor:", frame_no/(30.0 * processing_time))
    print("Time spent in os.system", tot_os_cmd_time)

if __name__ == "__main__":
    run_type = 1

    if run_type == 1:
        build_tree()
    elif run_type == 2:
        cProfile.run("build_tree()", "profilestats")
        p = pstats.Stats('profilestats')
        #p.strip_dirs().sort_stats('cumulative').print_stats()
        p.sort_stats('cumulative').print_stats()
    elif run_type ==3:
        profiler = cProfile.Profile()
        profiler.run("build_tree()")
        visualize(profiler.getstats())
        convert(profiler.getstats(), 'profiling_results.kgrind')
    else:
        print("provide valid run_type number")

###########PLAN REC: mk@rodeo:~/Planning/PlanRecGeffnerRamirez/plan-recognition/suboptimal$ python subopt_PR.py -s -e /home/mk/Planning/PlanRecGeffnerRamirez/aaai-10-benchmarks/block-words_p01_hyp-0_10_0.tar.bz2
#TODO --> maybe have dual tree that encodes action trace instead of state trace?
#TODO --> store more data in tree?
#TODO --> MCTS with plan rec (attention to impossible plans, what is the right high cost for impossible plans? 50?)
#TODO --> maybe make toy domain with a lower branching factor
#TODO --> os.system call to validate takes up almost all the run time (88%). Optimize for time here!
#   option 1: give multiple plan files per call. for each current state, give all plans at once
#   option 2: change VAL to keep running an take in new plans and current states, i.e., avoid reinitializing all the time
#TODO --> give time horizon for applicability of actions: remove "old nodes" from the open set
#   the though is, that maybe not every applied action is correct, but after a while, it is probable, that the initial state
#   is not the best state to apply a newly seen action to. it is more likely, that some of the previous actions were correct, hopefully
#TODO --> save current state files for reusage

#16:57 start zeit alter echtzeitfaktor 6.5