from datetime import datetime
import pic_to_plan_v2.observation_trace_gen.parse_ontology as parse_ontology_mod
import pic_to_plan_v2.observation_trace_gen.watch_video as watch_video_mod
import pic_to_plan_v2.uct.new_uct_dag as new_uct_dag_mod
import copy
import os
from pic_to_plan_v2.settings import ROOT_DIR as ROOT_DIR
from pathlib import Path
import shutil

def run_single_video(session_name):
    ###cleanup folders in prob_plan_recognition_X when search was interrupted
    #TODO

    start_time = datetime.now()
    #config_file_name = "no_preconditions_test.txt"
    #config_file_name = "cut_cucumber_bread_config_1_dummy_setting_ccb_minimal.txt"
    #config_file_name = "cut_cucumber_bread_config_1_dummy_setting.txt"
    #config_file_name = "ccb_minimal_domain_cut_graspable_config_1.txt"
    config_file_name = "complex-domain-test-series-"+session_name+"-reeval-test.txt"

    config_file_dir = os.path.join(ROOT_DIR, "experiment_configurations")
    config_file_path = os.path.join(config_file_dir, config_file_name)

    with open(config_file_path, "r") as f:
        for l in f:
            if l[0] != ";": #; denotes comment
                l = l.strip().split(" ")
                if l[0] == "experiment_name:":
                    experiment_name = (" ").join(l[1:])
                elif l[0] == "experiment_comment:":
                    experiment_comment = (" ").join(l[1:])
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

    print("Experiment name:", experiment_name)
    print("Experiment comment:", experiment_comment)
    print("Instance path:", instance_path)
    ###parse ontology
    #     reads in the ontology and fills in template-domain.pddl and template-instance.pddl as template-domain-inserted-predicates.pddl and
    #     template-instance.parsed.objects.pddl
    parse_ontology_mod.main_parse_ontology(ontology_path, domain_path, instance_path)

    ###watch video
    #     load the superclass and individual type dict via parse_ontology()
    #     find all touch events
    #     find all possible actions
    #ATTENTION: TODO
    # eventually, watch video must run, too. now it only needs to run, if the domain or ontology has changed
    #watch_video_mod.main_watch_video(domain_path, instance_path, session_name, ontology_path)
    domain_inserted_predicates_path = str(domain_path).replace(".pddl", "-inserted-predicates.pddl")
    instance_inserted_predicates_path = str(instance_path).replace(".pddl", "-parsed-objects.pddl")

    ###uct dag
    current_results_dir = str(results_dir / Path(experiment_name +"_"+str(datetime.now())))
    os.mkdir(current_results_dir)
    print("UCT Instantiation")
    uct_search = new_uct_dag_mod.UCT_Search(domain_inserted_predicates_path, instance_inserted_predicates_path, session_name, ontology_path, save_after_X_iterations, experiment_name, current_results_dir, goal_path, possible_actions_percentage)

    print("Start UCT Search")
    uct_search.search(copy.deepcopy(uct_search.current_state_set), time_limit=time)
    #change in uct_dag line 73ffff
    end_time = datetime.now()
    print("DONE", experiment_name, "\nStart:", start_time, "\nEnd:", end_time, "\nDuration:", end_time - start_time)
    uct_search.viz("test-viz-final"+ str(datetime.now()))
    uct_search.viz("viz-" + str(uct_search.n_iter))
    uct_search.save_nodes_and_edges()
    #uct_search.save_root_node(
    uct_search.save_UCT_DAG()

if __name__ == "__main__":
    sessions = ["s13-d21",
    "s13-d25",
    "s21-d21",
    "s22-d25",
    "s23-d21",
    "s27-d21",
    "s28-d25",
    "s31-d25",
    "s37-d21",
    "s37-d25"]

    sessions = ["s13-d21"]

    for s in sessions:
        run_single_video(s)
