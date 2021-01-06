from datetime import datetime
import pic_to_plan_v2.observation_trace_gen.parse_ontology as parse_ontology_mod
import pic_to_plan_v2.observation_trace_gen.watch_video_gsrl as watch_video_mod_gsrl
import pic_to_plan_v2.observation_trace_gen.watch_video_v4rvrk as watch_video_mod_v4rvrk
import pic_to_plan_v2.uct.new_uct_dag as new_uct_dag_mod
import copy
import os
from pic_to_plan_v2.settings import ROOT_DIR, set_args
import pic_to_plan_v2.settings as settings
from pathlib import Path
import shutil
import math
import configargparse

# what do i need for a general experiment:
# dataset
# sample
#   a video ###these 3 parameters will be set in a separate function wrt the defined dataset
#   bounding box descriptions
#   everything to resolve bounding box ids to ontology identifier
# ontology
# domain
# instance
# goal set
# possible actions #do i still need this?
# duration #how long this experiment will run. formerly called "time"
# save_after_X_iterations (int <= 1)
# plan_progress (0-1) #formerly possible_actions_percentage 0-100
# missing_actions_probability (0-1)


def run_single_video(config_file_name):
    # Cleanup folders in prob_plan_recognition_X when search was interrupted
    for folder in os.walk(Path(ROOT_DIR, "external/")):
        if folder[0].endswith("prob-0-PR") or folder[0].endswith("prob-1-PR"):
            print("Delete Folder", folder[0])
            shutil.rmtree(folder[0])

    start_time = datetime.now()

    config_file_dir = os.path.join(ROOT_DIR, "experiment_configurations")
    config_file_path = os.path.join(config_file_dir, config_file_name)

    parser = configargparse.ArgParser(description='Run Plan Recognition from Object Detection Traces for single video.')
    parser.add_argument('-c', '--config', is_config_file=True, help='config file path')
    parser.add_argument("--dataset", required=True, choices=["groundedsemanticrolelabeling", "v4rvrkitchenv1"],
                        help="which dataset is used")
    parser.add_argument("--sample", required=True, help="dataset sample path")
    parser.add_argument("--ontology", required=True, help="OWL ontology file")
    parser.add_argument("--domain", required=True, help="PDDL domain file")
    parser.add_argument("--instance", required=True, help="PDDL instance file")
    parser.add_argument("--goal_set", required=True, help="PDDL goal sets")
    parser.add_argument("--display_video",
                        help="shows the video when generating the possible actions",
                        action="store_true")
    parser.add_argument("--load_possible_actions",
                        help="loads the possible actions if they are already generated for this instance",
                        action="store_true")
    parser.add_argument("--duration", type=float, default=math.inf,
                        help="defines search duration in seconds")
    parser.add_argument("--save_every_X_iterations", type=int, default=math.inf,
                        help="save search results after this many iterations of MCTS")
    # TODO add exceptions when these arguments are first looked at
    parser.add_argument("--plan_progress", type=float, default=1.0,
                        help="how much from the start of the possible actions of this sample is used as input")
    parser.add_argument("--missing_action_probability", type=float, default=0.0,
                        help="how likely a possible action is not observed")
    parser.add_argument("--experiment_description",
                        help="describe what to achieve with this experiment")

    args = parser.parse_args()
    print(parser.format_values())

    # Instantiate the search, depending which dataset is chosen
    if args.dataset == "v4rvrkitchenv1":
        set_args(args)
    elif args.dataset == "groundedsemanticrolelabeling":
        with open(config_file_path, "r") as f:
            for l in f:
                if l[0] != ";":  # ; denotes comment
                    l = l.strip().split(" ")
                    if l[0] == "experiment_name:":
                        experiment_name = " ".join(l[1:])
                    elif l[0] == "experiment_comment:":
                        experiment_comment = " ".join(l[1:])
                    elif l[0] == "domain:":
                        domain_path = Path(ROOT_DIR) / Path(l[1])
                    elif l[0] == "instance:":
                        instance_path = Path(ROOT_DIR) / Path(l[1])
                    elif l[0] == "goals:":
                        goal_path = Path(ROOT_DIR) / Path(l[1])
                    elif l[0] == "ontology:":
                        ontology_path = Path(ROOT_DIR) / Path(l[1])
                    elif l[0] == "possible_actions:":
                        possible_actions_path = Path(ROOT_DIR) / Path(l[1])
                    elif l[0] == "time:":
                        time = int(l[1])
                        if time == -1:
                            time = None
                    elif l[0] == "results_dir:":
                        results_dir = Path(ROOT_DIR) / Path(l[1])
                    elif l[0] == "session_name:":
                        session_name = l[1]
                    elif l[0] == "save_after_X_iterations:":
                        save_after_X_iterations = int(l[1])
                    elif l[0] == "possible_actions_percentage:":
                        possible_actions_percentage = float(l[1])

    ontology_path = args.ontology
    domain_path = args.domain
    instance_path = args.instance
    sample_name = args.sample.split(os.sep)[-1]
    sample_file_path = args.sample

    # parse ontologya
    #     reads in the ontology and fills in template-domain.pddl and template-instance.pddl as template-domain-inserted-predicates.pddl and
    #     template-instance.parsed.objects.pddl

    parse_ontology_mod.main_parse_ontology(ontology_path, domain_path, instance_path)
    # watch video
    #     load the superclass and individual type dict via parse_ontology()
    #     find all touch events
    #     find all possible actions
    # ATTENTION: TODO
    # eventually, watch video must run, too. now it only needs to run, if the domain or ontology has changed
    if args.dataset == "groundedsemanticrolelabeling":
        watch_video_mod_gsrl.main_watch_video(domain_path, instance_path, sample_name, ontology_path)
    elif args.dataset == "v4rvrkitchenv1":
        # watch_video_mod_v4rvrk.main_watch_video(domain_path, instance_path, sample_name, ontology_path)
        print("SKIP WATCHING VIDEO")

    # these are the finished domain and instance paths
    domain_inserted_predicates_path = str(domain_path).replace(".pddl", "-inserted-predicates.pddl")
    instance_inserted_predicates_path = str(instance_path).replace(".pddl", "-parsed-objects.pddl")

    # uct dag
    current_results_dir = str(Path(ROOT_DIR, "data/results", sample_name + "_" +
                                   datetime.now().strftime("%Y_%m_%d-%H_%M_%S")))
    os.mkdir(current_results_dir)
    print("UCT Instantiation")  # second sample_name can be more descriptive experiment name
    uct_search = new_uct_dag_mod.UctSearch(domain_inserted_predicates_path,
                                           instance_inserted_predicates_path,
                                           sample_name,
                                           ontology_path,
                                           settings.ARGS.save_every_X_iterations,
                                           sample_name,
                                           current_results_dir,
                                           settings.ARGS.goal_set,
                                           settings.ARGS.plan_progress)

    print("Start UCT Search")
    uct_search.search(copy.deepcopy(uct_search.current_state_set), time_limit=settings.ARGS.duration)
    # change in uct_dag line 73ffff
    end_time = datetime.now()
    print("DONE", sample_name, "\nStart:", start_time, "\nEnd:", end_time, "\nDuration:", end_time - start_time)
    uct_search.viz("test-viz-final" + datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))
    uct_search.viz("viz-" + str(uct_search.n_iter))
    uct_search.save_nodes_and_edges()
    # uct_search.save_root_node(
    uct_search.save_uct_dag()


if __name__ == "__main__":
    # config files are stored in folder "experiment_configurations"
    config_file_name = "v4r_vr_kitchen_test.conf"
    run_single_video(config_file_name)

#
# output jan 6 test ramirez
#
# Time spent: 8.580 seconds
# HERE2
# MOVING PROB PR TO PROB INDEX PR
# ('CURRENT', '/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/external/prob_plan_recognition_0')
# Timeout: 457 seconds
# Heap restriction: 7168 MB
# Command: (../downward/fast-downward.py prob-3-PR/O/pr-domain.pddl prob-3-PR/O/pr-problem.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])") >> pr-problem-3-O.log 2>&1
#
#
# Time spent: 67.220 seconds
# Timeout: 847 seconds
# Heap restriction: 7168 MB
# Command: (../downward/fast-downward.py prob-3-PR/neg-O/pr-domain.pddl prob-3-PR/neg-O/pr-problem.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])") >> pr-problem-3-neg-O.log 2>&1
#
#
# Time spent: 67.260 seconds
# domain.pddl
# hyp_0_problem.pddl
# hyp_1_problem.pddl
# hyp_2_problem.pddl
# hyp_3_problem.pddl
# template.pddl
# domain.pddl_hyp_0_problem.pddl_obs.dat_transcription.log
# domain.pddl_hyp_1_problem.pddl_obs.dat_transcription.log
# domain.pddl_hyp_2_problem.pddl_obs.dat_transcription.log
# domain.pddl_hyp_3_problem.pddl_obs.dat_transcription.log
# pr-problem-0-O.log
# pr-problem-0-neg-O.log
# pr-problem-1-O.log
# pr-problem-1-neg-O.log
# pr-problem-2-O.log
# pr-problem-2-neg-O.log
# pr-problem-3-O.log
# pr-problem-3-neg-O.log
# report.txt
# obs.dat
# hyps.dat
# prob-0-PR/
# prob-0-PR/O/
# prob-0-PR/O/pr-problem.pddl
# prob-0-PR/O/pr-domain.pddl
# prob-0-PR/neg-O/
# prob-0-PR/neg-O/pr-problem.pddl
# prob-0-PR/neg-O/pr-domain.pddl
# prob-1-PR/
# prob-1-PR/O/
# prob-1-PR/O/pr-problem.pddl
# prob-1-PR/O/pr-domain.pddl
# prob-1-PR/neg-O/
# prob-1-PR/neg-O/pr-problem.pddl
# prob-1-PR/neg-O/pr-domain.pddl
# prob-2-PR/
# prob-2-PR/O/
# prob-2-PR/O/pr-problem.pddl
# prob-2-PR/O/pr-domain.pddl
# prob-2-PR/neg-O/
# prob-2-PR/neg-O/pr-problem.pddl
# prob-2-PR/neg-O/pr-domain.pddl
# prob-3-PR/
# prob-3-PR/O/
# prob-3-PR/O/pr-problem.pddl
# prob-3-PR/O/pr-domain.pddl
# prob-3-PR/neg-O/
# prob-3-PR/neg-O/pr-problem.pddl
# prob-3-PR/neg-O/pr-domain.pddl
# max prob 0.268941
# duration 613.5336368083954
# DET VALS [9.0, 8.0, 0.2689409852027893, 9.0, 8.0, 0.2689409852027893, 12.0, 11.0, 0.2689409852027893, 20.0, 19.0, 0.2689409852027893]
#
# Process finished with exit code 0

#output in report.txt in ramirez method (other example)
# Experiment=/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/pr_instance_1.tar.bz2
# Num_Hyp=2
# Hyp_Atoms=(cut cucumber_1)
# Hyp_Test_Failed=False
# Hyp_Cost_O=15.000000
# Hyp_Cost_Not_O=7.000000
# Hyp_Prob_O=0.000335
# Hyp_Prob_Not_O=0.999665
# Hyp_Plan_Time_O=10.610000
# Hyp_Plan_Time_Not_O=10.610000
# Hyp_Trans_Time=2.060000
# Hyp_Plan_Time=21.220000
# Hyp_Test_Time=23.280000
# Hyp_Is_True=False
# Hyp_Atoms=(cut bun_1)
# Hyp_Test_Failed=False
# Hyp_Cost_O=15.000000
# Hyp_Cost_Not_O=7.000000
# Hyp_Prob_O=0.000335
# Hyp_Prob_Not_O=0.999665
# Hyp_Plan_Time_O=10.870000
# Hyp_Plan_Time_Not_O=11.020000
# Hyp_Trans_Time=1.070000
# Hyp_Plan_Time=21.890000
# Hyp_Test_Time=22.960000
# Hyp_Is_True=False