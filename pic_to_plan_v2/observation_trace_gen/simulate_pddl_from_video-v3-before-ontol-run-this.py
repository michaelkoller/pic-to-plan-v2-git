import pickle
from .parsed_proplem import ParsedPDDLProblem
from .video_annotation import VideoAnnotation
import os
import re
import time
from treelib import Node, Tree
import copy

t0 = time.time()
my_parsed_problem = ParsedPDDLProblem("take-put-domain-v1.pddl", "take-put-instance-v1.pddl")

# dict from bounding boxes to parsed_problem_objects_dict.keys()
bb_to_pddl_obj_dict = {'r_hand': 'r_hand', 'l_hand': 'l_hand', 'plastic_paper_bag': 'plastic_paper_bag1',
                       'plate': 'plate1', \
                       'knife': 'knife1', 'cuttingboard': 'cuttingboard1', 'cupboard': 'cupboard1',
                       'counter': 'counter1', \
                       'drawer': 'drawer1', 'drawer': 'drawer2', 'bread': 'bread1', 'bread': 'bread2',
                       'bread': 'bread3', 'sponge':'sponge1', 'faucet':'faucet1', 'towel':'towel1', \
                       'g_drawer':'g_drawer1','g_drawer1':'g_drawer11', 'fridge' : 'fridge1', 'sink': 'sink1', \
                       'cucumber':'cucumber1', 'bowl': 'bowl1', 'peeler': 'peeler1', 'peel': 'peel1', 'end':'end1', \
                       'spice_shaker': 'spice_shaker1', 'spice_holder': 'spice_holder1', 'spice':'spice1', \
                       'plastic_bag':'plastic_bag1'}

video_annotation = VideoAnnotation(
    '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/Videos/', \
    '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/')

session_name = "s13-d25"
t_start = time.time()
print(session_name)
detected_added_touches_session = pickle.load( open("detected_added_touches_session_"+session_name+".p", "rb" ) )
detected_added_touches_w_hand_session = pickle.load( open("detected_added_touches_w_hand_session_"+session_name+".p", "rb" ) )
possible_actions_session = pickle.load( open("possible_actions_session_"+session_name+".p", "rb" ) )



#lama2011: /home/mk/Planning/fastdownwardplanner/fast-downward.py  --alias seq-sat-lama-2011 /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl

# cmd = '/home/mk/Planning/fastdownwardplanner/fast-downward.py --validate /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl --search "astar(lmcut())" > fast_downward_out.txt'

#get current state from parsed problem
current_state_FD = my_parsed_problem.parsed_problem_FD.init
current_state_set = set()
for atom in current_state_FD:
    if atom.predicate != "=":
        s = "("+ str(atom.predicate) + " " + " ".join(atom.args) + ")"
        current_state_set.add(s)
        print(s)
current_state_string = " ".join(sorted(current_state_set))

#put init state at root of tree
#https://treelib.readthedocs.io/en/latest/
tree = Tree()
tree.create_node(str(current_state_string), 0, data=[current_state_set, ""]) #in the root there was no previous action
open_state_set = [0]  #put the initial state as first element into the open state set
state_string_to_node_id_dict = dict()
state_string_to_node_id_dict[str(current_state_string)] = 0

#TODO put "some" current state into the template, not only the init state
template_instance = open("template-instance-v1.pddl", "r")
template_instance_string = "".join(template_instance.readlines())
parsed_template_instance_string = template_instance_string.replace("<insert_init>", "\n".join(current_state_string))
f = open("current-state-take-put-instance.pddl", "w")
f.write(parsed_template_instance_string)
f.close()

tree_id_counter = 1
tree.show()
for timestep in possible_actions_session:
    frame_no = timestep[0]
    open_state_set_for_timestep = []
    for try_action in timestep[1]:
        for s in open_state_set:
            try_action_string = "(" + " ".join(try_action) + ")"    #create the plan for the action to try
            f = open("current_sas_plan_try", "w")
            f.write(try_action_string + "\n;cost = 1 (unit cost)")
            f.close()

            current_state_set = tree[s].data[0]
            current_state_string = " ".join(current_state_set)

            template_instance = open("template-instance-v1.pddl", "r") #create the current state problem instance
            template_instance_string = "".join(template_instance.readlines())
            parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
            f = open("current-state-take-put-instance.pddl", "w")
            f.write(parsed_template_instance_string)
            f.close()

            #print("VALIDATE PLAN")
            cmd = '/home/mk/Planning/VAL/validate -v  /home/mk/PycharmProjects/pic-to-plan/take-put-domain-v1.pddl /home/mk/PycharmProjects/pic-to-plan/current-state-take-put-instance.pddl current_sas_plan_try > plan_val_output.txt'
            #cmd = '/home/mk/Planning/VAL/validate -v  /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/current-state-take-put-instance-no-handempty.pddl /home/mk/PycharmProjects/pic-to-plan/val_exp/open_sas_plan > plan_val_output.txt' #check for unsatisfied precondition --> action not applicable in current state
            os.system(cmd)
            plan_val_output = open("plan_val_output.txt", "r")
            plan_val_output_joined = "".join(plan_val_output.readlines())
            #print(plan_val_output_joined)

            new_state_set = copy.deepcopy(current_state_set)
            plan_val_output = open("plan_val_output.txt", "r")
            for line in plan_val_output:
                if "Deleting" in line:
                    m = re.search(r"\([A-Za-z0-9_ ]+\)", line)
                    atom_to_delete = m.group(0)
                    #print("DEL", atom_to_delete)
                    if atom_to_delete in new_state_set:
                        new_state_set.remove(atom_to_delete)
                elif "Adding" in line:
                    m = re.search(r"\([A-Za-z0-9_ ]+\)", line)
                    atom_to_add = m.group(0)
                    #print("ADD", atom_to_add)
                    if atom_to_add not in new_state_set:
                        new_state_set.add(atom_to_add)
            sorted_new_state_string = " ".join(sorted(new_state_set))
            if sorted_new_state_string not in state_string_to_node_id_dict.keys():
                tree.create_node(sorted_new_state_string, tree_id_counter, data=[new_state_set, try_action_string], parent=tree[s].identifier) #in the root there was no previous action
                open_state_set_for_timestep.append(tree_id_counter)
                state_string_to_node_id_dict[sorted_new_state_string] = tree_id_counter
                tree_id_counter += 1
            t1 = time.time()
            if t1-t0 > 60:
                t0 = t1
                tree.show()
                print(frame_no, tree_id_counter)

    open_state_set.extend(open_state_set_for_timestep)
tree.show()
t_stop = time.time()
processing_time = t_stop - t_start
print("FINISHED", "Frame no:", frame_no, "Node count:", tree_id_counter, "Tree depth:", tree.depth())
print("Processing time:", processing_time, "Video length:", frame_no/30.0, "Realtime factor:", frame_no/(30.0 * processing_time))

###########PLAN REC: mk@rodeo:~/Planning/PlanRecGeffnerRamirez/plan-recognition/suboptimal$ python subopt_PR.py -s -e /home/mk/Planning/PlanRecGeffnerRamirez/aaai-10-benchmarks/block-words_p01_hyp-0_10_0.tar.bz2
