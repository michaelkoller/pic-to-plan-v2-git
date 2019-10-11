import pickle
import pic_to_plan_v2.uct.uct_node as un
import pic_to_plan_v2.uct.uct_edge as ue
import pic_to_plan_v2.uct.uct_dag as ud


def backup(edge_descent_trace, delta):
    for e in edge_descent_trace[::-1]:
        e.total_reward += delta
        e.num_visits += 1

root = pickle.load( open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/results/ccb_minimal_cut_graspable_test_exp_2019-09-15 14:01:49.409688/root_node_ccb_minimal_cut_graspable_test_exp_3711.p", "rb" ))
print(root)
print(root.get_best_child(d_1=-1, d_2=0, d_3=0, exploration_value=0))
print(root.get_best_child(d_1=1, d_2=0, d_3=0, exploration_value=0))
print(root.get_best_child(d_1=0, d_2=0, d_3=0, exploration_value=0))
print(root.get_best_child(d_1=-1, d_2=0, d_3=0, exploration_value=0))
print(root.get_best_child(d_1=2, d_2=0, d_3=0, exploration_value=0))
print(root.in_edges[0].get_mean_reward())

#when exploration value = 0, d_2 and d_3 don't matter

new_root = un.Node(["None"], None, None, None, None)
new_root_in_edge = ue.Edge(None, new_root, None, 0)
new_root.in_edges = [new_root_in_edge]

e_1 = ue.Edge(new_root, None, None, None)
n_1 = un.Node(["N1"], e_1, None, None, None)
e_1.destination = n_1
new_root.out_edges.append(e_1)

e_2 = ue.Edge(new_root, None, None, None)
n_2 = un.Node(["N2"], e_2, None, None, None)
e_2.destination = n_2
new_root.out_edges.append(e_2)

e_3 = ue.Edge(n_1, None, None, None)
n_3 = un.Node(["N3"], e_3, None, None, None)
e_3.destination = n_3
n_1.out_edges.append(e_3)

e_4 = ue.Edge(n_2, None, None, None)
n_4 = un.Node(["N4"], e_4, None, None, None)
e_4.destination = n_4
n_2.out_edges.append(e_4)


e_1_reward = 1
e_2_reward = 0
e_3_reward = 0
e_4_reward = 2

backup([e_1], e_1_reward)
backup([e_1, e_3], e_2_reward)
backup([e_2], e_3_reward)
backup([e_2, e_4], e_4_reward)
e_1.mu_prime = e_1_reward
e_1.n_prime = 1
e_2.mu_prime = e_2_reward
e_2.n_prime = 1
e_3.mu_prime = e_3_reward
e_3.n_prime = 1
e_4.mu_prime = e_4_reward
e_4.n_prime = 1

print(new_root)
print("best child from root")
print(new_root.get_best_child(d_1=-1, d_2=0, d_3=0, exploration_value=0))

print("e-1 mu", e_1.get_mu(-1))
print("e-2 mu", e_2.get_mu(-1))
print("e-4 mu", e_4.get_mu(-1))
