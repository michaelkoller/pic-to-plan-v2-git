import pickle
import os
experiment_folder_name = "/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/data/results/Sample2020-11-07-17_50_50_2020-12-07%2021:17:05.796245/"
experiment_name = "Sample2020-11-07-17_50_50_0"
iter = 373
out_edge_dict = pickle.load( open(r"/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/data/results/Sample2020-11-07-17_50_50_2020-12-07 20:21:17:05.796245/out_edge_dict_Sample2020-11-07-17_50_50_0.p", "rb" ) )
exit()
#out_edge_dict = pickle.load( open( experiment_folder_name + "out_edge_dict_"+str(experiment_name)+"_"+str(iter)+".p", "rb" ) )
in_edge_dict = pickle.load( open( experiment_folder_name + "in_edge_dict_"+str(experiment_name)+"_"+str(iter)+".p", "rb" ) )
node_dict = pickle.load( open( experiment_folder_name + "node_dict_"+str(experiment_name)+"_"+str(iter)+".p", "rb" ) )

current_node = "(hand_empty l_hand) (hand_empty r_hand)"
current_edge = None #graph[0].obj_dict['edges'][('0','3')][0]['name']
current_edge_label = None #graph[0].obj_dict['edges'][('0','3')][0]['attributes']['label']

original_root_node = pickle.load( open( experiment_folder_name + "root_node_"+str(experiment_name)+"_"+str(iter)+".p", "rb" ) )

#list all goal states
#goals = ["(used plastic_paper_bag1)", "(used plate1)", "(used knife1)", "(used cuttingboard1)"]
goals = ["(cut cucumber_1)"]
goal_state_number = 0
for n in node_dict:
    if n != "node":
        state = node_dict[n].state
        no_goals_list = [y in state for y in goals]
        no_goal_facts_true = no_goals_list.count(True)
        if no_goal_facts_true >= 3:
            print(no_goal_facts_true, "out of", len(goals), "reached in ")
            print(n, node_dict[n])
        if all(x in node_dict[n].state for x in goals):
            print("ABSOLUTE GOAL REACHED")
            goal_state_number += 1
            print(n, node_dict[n])


roo = node_dict["(hand_empty l_hand) (hand_empty r_hand)"]
ooo = node_dict["(grasped bread1) (grasped knife1) (in_hand bread1 r_hand) (in_hand knife1 l_hand)"]
nnn = node_dict["(grasped bread1) (grasped knife1) (in_hand bread1 l_hand) (in_hand knife1 r_hand)"]
nnnn = out_edge_dict["(grasped bread1) (grasped knife1) (in_hand bread1 l_hand) (in_hand knife1 r_hand)"]
mmmkr = node_dict["(cut bread1) (grasped bread1) (grasped knife1) (in_hand bread1 l_hand) (in_hand knife1 r_hand)"]
mmmkl = node_dict["(cut bread1) (grasped bread1) (grasped knife1) (in_hand bread1 r_hand) (in_hand knife1 l_hand)"]
omom = node_dict["(grasped plastic_paper_bag1) (hand_empty r_hand) (in_hand plastic_paper_bag1 l_hand)"]
print("GOAL STATES")
print(goal_state_number,  "/", len(node_dict))
direction = "down"
chosen_next_node = None
while chosen_next_node != "exit":
    eee = []
    if direction == "down":
        if current_node in out_edge_dict:
            for [to_state_string, edge] in out_edge_dict[current_node]:
                eee.append([to_state_string, edge.action, edge, round(edge.saved_saff_mu_val,3), round(edge.get_normal_mean_reward(),3), round(edge.mu_prime, 3),  3])
        else:
            print("NO EDGES IN DOWN DIRECTION FROM HERE")
    elif direction == "up":
        if current_node in in_edge_dict:
            for [to_state_string, edge] in in_edge_dict[current_node]:
                eee.append([to_state_string, edge.action, edge, round(edge.mu_prime, 3), round(edge.total_reward/edge.num_visits, 3)])
        else:
            print("NO EDGES IN UP DIRECTION FROM HERE")
    eee = sorted(eee, key=lambda tup: tup[3], reverse=True)
    print("CHOOSE AMONG THESE (1st argument is key)")
    for e in eee:
        e = map(str, e)
        print(";\t".join(e))
    print("INPUT NEXT NODE NUMBER | jump | up | down:")
    chosen_next_node = input()
    if chosen_next_node != "jump" and chosen_next_node != "up" and chosen_next_node != "down":
        if direction == "down":
            a = current_node
            b = chosen_next_node
        elif direction == "up":
            b = current_node
            a = chosen_next_node
        print("STATE", node_dict[chosen_next_node])
        current_node = chosen_next_node
    elif chosen_next_node == "jump":
        print("INPUT NODE NUMBER TO JUMP TO:")
        current_node = input()
        print("STATE", node_dict[current_node])
    elif chosen_next_node == "up":
        direction = "up"
        print("DIRECTION UP")
    elif chosen_next_node == "down":
        direction = "down"
        print("DIRECTION DOWN")
    else:
        print("NO VALID ACTION TAKEN")

