import pickle
iter = 6

n = pickle.load( open( "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/node_dict"+str(iter)+".p", "rb" ) )
i = pickle.load( open( "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/in_edge_dict"+str(iter)+".p", "rb" ) )
o = pickle.load( open( "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/out_edge_dict"+str(iter)+".p", "rb" ) )

print("NODES")
print(n)

print("IN")
print(i)

print("OUT")
print(o)
