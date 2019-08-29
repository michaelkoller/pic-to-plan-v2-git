import pydot

graph = pydot.graph_from_dot_file("nx_1160.dot")
print(graph)
print(graph[0].obj_dict['nodes'])
print(graph[0].obj_dict['edges'])


n = graph[0].obj_dict['nodes']['0'][0]['attributes']['num_visits']

edges = graph[0].obj_dict['edges']
edge_dict = {}
for (p,c) in edges:
    if p in edge_dict:
        edge_dict[p].append(c)
    else:
        edge_dict[p] = [c]

current_node = graph[0].obj_dict['nodes']['0'][0]['name']
while current_node in edge_dict:
    print("--------------")
    print(current_node)
    print(float(graph[0].obj_dict['nodes'][current_node][0]['attributes']['total_reward']) / float(graph[0].obj_dict['nodes'][current_node][0]['attributes']['num_visits']))
    print(graph[0].obj_dict['nodes'][current_node][0]['attributes']['prev_action'])
    best_reward = 0
    best_next_node = None
    for x in edge_dict[current_node]:
        child_reward = float(graph[0].obj_dict['nodes'][c][0]['attributes']['total_reward']) / float(graph[0].obj_dict['nodes'][c][0]['attributes']['num_visits'])
        if child_reward >= best_reward:
            best_reward = child_reward
            best_next_node = x
    current_node = x

#print(graph[0].obj_dict['nodes']['0']['attributes'])
#print(graph[0].obj_dict['nodes']['0']['total_reward'])
#print(graph[0].obj_dict['nodes']['0']['num_visits'])

