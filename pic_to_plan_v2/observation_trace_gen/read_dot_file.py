import pydot

graph = pydot.graph_from_dot_file("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/nx_1640.dot")
print(graph)
print(graph[0].obj_dict['nodes'])
print(graph[0].obj_dict['edges'])

n = graph[0].obj_dict['nodes']['0'][0]['attributes']['num_visits']

edges = graph[0].obj_dict['edges']
in_edge_dict = {}
out_edge_dict = {}
for (p,c) in edges:
    if p in out_edge_dict:
        out_edge_dict[p].append(c)
    else:
        out_edge_dict[p] = [c]
    if c in in_edge_dict:
        in_edge_dict[c].append(p)
    else:
        in_edge_dict[c] = [p]

print(graph[0].obj_dict['edges'][('0','3')][0]['attributes']['saffidine_mu'])

current_node = graph[0].obj_dict['nodes']['0'][0]['name']
current_edge = None #graph[0].obj_dict['edges'][('0','3')][0]['name']
current_edge_label = None #graph[0].obj_dict['edges'][('0','3')][0]['attributes']['label']
print(current_node)
print(current_node in out_edge_dict)
print(out_edge_dict[current_node])
print(graph[0].obj_dict['nodes']['0'][0]['attributes']['state'])

#list all goal states
goals = ["(used plastic_paper_bag1)", "(used plate1)", "(used knife1)", "(used cuttingboard1)"]
goal_state_number = 0
for n in graph[0].obj_dict['nodes']:
    if n != "node":
        if all(x in graph[0].obj_dict['nodes'][n][0]['attributes']['state'] for x in goals):
            goal_state_number += 1
            print(graph[0].obj_dict['nodes'][n][0]['name'], graph[0].obj_dict['nodes'][n][0])
            print(graph[0].obj_dict['nodes'][n][0]['name'], graph[0].obj_dict['nodes'][n][0]['attributes']['state'])
print(goal_state_number,  "/", len(graph[0].obj_dict['nodes']))
direction = "down"
chosen_next_node = None
while chosen_next_node != "exit":
    eee = []
    if direction == "down":
        if current_node in out_edge_dict:
            for e in out_edge_dict[current_node]:
                eee.append([e, graph[0].obj_dict['edges'][(current_node, e)][0]['attributes']['label'], "\n", \
                        float(graph[0].obj_dict['edges'][(str(current_node),str(e))][0]['attributes']['saffidine_mu']), \
                        float(graph[0].obj_dict['edges'][(str(current_node),str(e))][0]['attributes']['mean_reward'])])
        else:
            print("NO EDGES IN DOWN DIRECTION FROM HERE")
    elif direction == "up":
        if current_node in in_edge_dict:
            for e in in_edge_dict[current_node]:
                eee.append([e, graph[0].obj_dict['edges'][(e, current_node)][0]['attributes']['label'], "\n", \
                        float(graph[0].obj_dict['edges'][(str(e), str(current_node))][0]['attributes']['saffidine_mu']), \
                        float(graph[0].obj_dict['edges'][(str(e),str(current_node))][0]['attributes']['mean_reward'])])
        else:
            print("NO EDGES IN UP DIRECTION FROM HERE")
    eee = sorted(eee, key=lambda tup: tup[3], reverse=True)
    for e in eee:
        e = map(str, e)
        print(" ".join(e))
    print("INPUT NEXT NODE NUMBER | jump | up | down:")
    chosen_next_node = input()
    if chosen_next_node.isdigit():
        if direction == "down":
            a = current_node
            b = chosen_next_node
        elif direction == "up":
            b = current_node
            a = chosen_next_node
        print("ACTION", graph[0].obj_dict['edges'][(a, b)][0]['attributes']['label'])
        print("STATE", graph[0].obj_dict['nodes'][a][0]['attributes']['label'])
        print("STATE", graph[0].obj_dict['nodes'][a][0]['attributes']['state'])
        current_node = chosen_next_node
    elif chosen_next_node == "jump":
        print("INPUT NODE NUMBER TO JUMP TO:")
        current_node = input()
        print("STATE", graph[0].obj_dict['nodes'][current_node][0]['attributes']['label'])
        print("STATE", graph[0].obj_dict['nodes'][current_node][0]['attributes']['state'])
    elif chosen_next_node == "up":
        direction = "up"
        print("DIRECTION UP")
    elif chosen_next_node == "down":
        direction = "down"
        print("DIRECTION DOWN")
# while current_node in out_edge_dict:
#     print("--------------")
#     print(current_node)
#     #print(float(graph[0].obj_dict['nodes'][current_node][0]['attributes']['total_reward']) / float(graph[0].obj_dict['nodes'][current_node][0]['attributes']['num_visits']))
#     #print(graph[0].obj_dict['nodes'][current_node][0]['attributes']['prev_action'])
#     best_reward = 0
#     best_next_node = None
#     best_next_edge = None
#     for e in out_edge_dict[current_node]:
#         #child_reward = float(graph[0].obj_dict['nodes'][e][0]['attributes']['total_reward']) / float(graph[0].obj_dict['nodes'][e][0]['attributes']['num_visits'])
#         edge_reward = float(graph[0].obj_dict['edges'][(str(current_node),str(e))][0]['attributes']['saffidine_mu'])
#         if edge_reward >= best_reward:
#             best_reward = edge_reward
#             best_next_edge = (str(current_node), str(e))
#             best_next_node = e
#     print("ACTION", graph[0].obj_dict['edges'][(current_node, best_next_node)][0]['attributes']['label'])
#     current_node = best_next_node
#
# #print(graph[0].obj_dict['nodes']['0']['attributes'])
# #print(graph[0].obj_dict['nodes']['0']['total_reward'])
# #print(graph[0].obj_dict['nodes']['0']['num_visits'])
#

