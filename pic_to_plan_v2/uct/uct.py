from pic_to_plan_v2.uct.uct_node import Node
import time
import math
import pickle
import re
import pic_to_plan_v2.observation_trace_gen.parsed_proplem as parsed_problem_mod
import pic_to_plan_v2.observation_trace_gen.video_annotation as video_annotation_mod
import os
import copy
import cProfile
import pstats
from pyprof2calltree import convert, visualize
import networkx as nx
import matplotlib.pyplot as plt
import pic_to_plan_v2.observation_trace_gen.draw_search_tree as draw_search_tree_mod
import pic_to_plan_v2.observation_trace_gen.create_pr_instance as create_pr_instance_mod
import pic_to_plan_v2.observation_trace_gen.call_plan_rec as call_plan_rec_mod

class UCTSearch:
    def __init__(self):
        self.t_start = time.time()

        # compile re for later use
        self.re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)")

        self.my_parsed_problem = parsed_problem_mod.ParsedPDDLProblem(
            "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl", \
            "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects.pddl")
        # dict from bounding boxes to parsed_problem_objects_dict.keys()
        self.bb_to_pddl_obj_dict = {'plastic_bag': ['plastic_bag1'], 'plastic_paper_bag': ['plastic_paper_bag1'],
                               'g_drawer': ['g_drawer1'],
                               'sponge': ['sponge1'], 'drawer': ['drawer1', 'drawer2'],
                               'cuttingboard': ['cuttingboard1'], 'end': ['end1'],
                               'bowl': ['bowl1'], 'r_hand': ['r_hand'], 'bread': ['bread1', 'bread2', 'bread3'],
                               'knife': ['knife1'], 'plate': ['plate1'],
                               'cupboard': ['cupboard1'], 'peel': ['peel1'], 'fridge': ['fridge1'],
                               'cucumber': ['cucumber1'], 'sink': ['sink1'],
                               'peeler': ['peeler1'], 'spice': ['spice1'], 'faucet': ['faucet1'],
                               'spice_holder': ['spice_holder1'],
                               'towel': ['towel1'], 'counter': ['counter1'], 'spice_shaker': ['spice_shaker1'],
                               'l_hand': ['l_hand'],
                               'g_drawer1': ['g_drawer11']}

        self.video_annotation = video_annotation_mod.VideoAnnotation(
            '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/Videos/', \
            '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/', \
            self.bb_to_pddl_obj_dict)

        self.session_name = "s13-d25"
        print(self.session_name)
        self.touch_events = pickle.load(open(
            "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/overlap_detections/touch_events_" + self.session_name + ".p",
            "rb"))
        self.possible_actions_session = pickle.load(open(
            "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_" + self.session_name + ".p",
            "rb"))

        # lama2011: /home/mk/Planning/fastdownwardplanner/fast-downward.py  --alias seq-sat-lama-2011 /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl
        # cmd = '/home/mk/Planning/fastdownwardplanner/fast-downward.py --validate /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl --search "astar(lmcut())" > fast_downward_out.txt'

        # get current state from parsed problem
        self.current_state_FD = self.my_parsed_problem.parsed_problem_FD.init
        self.current_state_set = set()
        for atom in self.current_state_FD:
            if atom.predicate != "=" and self.my_parsed_problem.onto[
                atom.predicate] is None:  # TODO only add non-static atoms (static atoms defined in domain need to be checked, too?)
                s = "(" + str(atom.predicate) + " " + " ".join(atom.args) + ")"
                self.current_state_set.add(s)

    def uct_search(self, s_0, possible_actions, iteration_limit=None, time_limit=None):
        """ s_0                 ... initial state
            possible_actions    ... action candidates, [(fram_no, [actions], (...), ...)]
                                    these are not necessarily applicable in a given state.
                                    check with VAL to get applicable actions for a state from possible actions"""
        self. s_0 = s_0
        self.v_0 = Node(self.s_0, None, possible_actions, None, 0)
        self.t_start = time.time()
        self.n_iter = 0
        self.iteration_limit = iteration_limit if iteration_limit != None else  math.inf
        self.time_limit = time_limit if time_limit != None else math.inf
        self.max_tree_depth = len(possible_actions) #there are no more observed actions from the bounding box overlaps after that.
                                                    #the tree at max level cannot be expanded further
                                                    #at max level you can only call default policy
        self.v_0.untried_children = self.v_0.call_VAL(possible_actions[0][1]) + [Node(self.v_0.state, self.v_0, self.v_0.possible_actions, "nop", self.v_0.depth + 1)]

        # t_1 = time.time()
        while (time.time()-self.t_start < self.time_limit and self.n_iter < self.iteration_limit):
            # if time.time() - t_1 > 10:
            #     t_1 = time.time()
            #     self.v_0.print_subtree()

            if self.n_iter % 10 == 0:
                self.save_dot()

            v_l = self.tree_policy(self.v_0)
            delta = self.default_policy(v_l)
            print(v_l.nid, v_l.prev_action, v_l.total_reward, delta)
            self.backup(v_l, delta)
            self.n_iter += 1
        self.v_0.print_subtree()
        self.get_best_path()
        t_stop = time.time()
        processing_time = t_stop - self.t_start
        print("FINISHED", "Frame no:", str(self.possible_actions_session[-1][0]), "Node count:", str(Node.nid))
        print("Processing time:", processing_time, "Video length:", self.possible_actions_session[-1][0] / 30.0, "Realtime factor:",
              self.possible_actions_session[-1][0] / (30.0 * processing_time))
        return 0

    def save_dot(self):
        G = uct_search.create_nx_graph()
        draw_search_tree_mod.draw_tree_nx(G, self.n_iter)

    def tree_policy(self, v):
        while not v.is_terminal:
            if v.depth == self.max_tree_depth - 1:
                return v
            elif not v.is_fully_expanded():
                expanded_v =  self.expand(v)
                return expanded_v
            else:
                v = v.get_best_child()
        return v #currently never reached, because no useful "is_terminal" definable

    def expand(self, v):
        if v.untried_children is None:
            v.untried_children = v.get_children_from_possible_actions() #call to VAL
        v_child =  v.choose_untried_action()
        return v_child

    def default_policy(self, v):
        if v.prev_action == "nop":
            #variant 1: prefers nop actions
            #return v.parent.total_reward #TODO can you do it just like that??? avoid plan rec in nop action states, since nothing has changed anyway
            #should be neutral: both num_visits and total_rewards increase. asymptotically same, but in the beginning, nop-actions are probably not prefered?
            return 1
            #return 0 --> this will inhibit use of nops
        else:
            obs = []
            while True:
                if v.parent is not None:
                    if v.prev_action != "nop":
                        obs.append(v.prev_action)
                    v = v.parent
                else:
                    break
            obs.reverse()
            create_pr_instance_mod.create_pr_instance(obs)
            return call_plan_rec_mod.call_plan_rec()

    def backup(self, v, delta):
        while v is not None:
            v.num_visits += 1
            v.total_reward += delta
            v = v.parent

    def get_best_path(self):
        path = [self.v_0]
        while path[-1].children is not None and len(path[-1].children)>0:
            v_child = path[-1].get_best_child(0) #no more exploration
            path.append(v_child)
        for v in path:
            print(str(v))

    def create_nx_graph(self):
        G = nx.DiGraph()

        def get_nx_nodes_a_edges(v, G):
            G.add_node(v.nid)
            if v.prev_action == "nop":
                G.node[v.nid]['color'] = 'red'
                G.node[v.nid]['fillcolor'] = 'red'
            else:
                G.node[v.nid]['color'] = 'black'
                G.node[v.nid]['fillcolor'] = 'white'
            G.node[v.nid]["penwidth"] = 5 * (v.total_reward / v.num_visits) if v.num_visits > 0 else 1
            G.node[v.nid]["total_reward"] = v.total_reward
            G.node[v.nid]["num_visits"] = v.num_visits
            G.node[v.nid]["prev_action"] = v.prev_action
            G.node[v.nid]["nid"] = v.nid
            G.node[v.nid]["parent_nid"] = v.parent.nid if v.parent is not None else "root"
            G.node[v.nid]["depth"] = v.depth
            G.node[v.nid]["label"] = "id"+str(v.nid)+" "+str(v.prev_action) + "\n" +str(v.num_visits) + " "+ str(round(v.total_reward,3)) + " " + str(round(v.total_reward/v.num_visits,3))

            for c in v.children.values():
                G.add_edge(v.nid, c.nid)
                G.edges[v.nid, c.nid]['penwidth'] = 5 * (c.total_reward / c.num_visits)
                get_nx_nodes_a_edges(c, G)
        get_nx_nodes_a_edges(self.v_0, G)
        return G

if __name__ == "__main__":
    # G = nx.DiGraph()
    # G.add_node(1)
    # G.add_node(2)
    # G.add_node(3)
    # G.add_edge(1,2)
    # G.add_edge(1,3)
    # G.edges[1,2]['penwidth'] = 3
    # print(G.edges[1,2])
    # print(G.edges)
    # exit()
    run_type = 1 #"test_put"
    uct_search = UCTSearch()

    if run_type == 1:
        uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), uct_search.possible_actions_session)
    elif run_type == 2:
        cProfile.run("uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), uct_search.possible_actions_session, iteration_limit=10)", "profilestats")
        p = pstats.Stats('profilestats')
        # p.strip_dirs().sort_stats('cumulative').print_stats()
        p.sort_stats('cumulative').print_stats()
    elif run_type == 3:
        profiler = cProfile.Profile()
        profiler.run("uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), uct_search.possible_actions_session, iteration_limit=10)")
        visualize(profiler.getstats())
        convert(profiler.getstats(), 'profiling_results.kgrind')
    elif run_type == "test_put":
        p_a = [(342, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (372, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (379, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (386, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (438, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (490, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (492, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (524, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (527, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (528, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (531, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (759, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (786, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (787, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (794, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (805, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (819, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (821, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (822, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (831, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (842, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (868, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (892, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (897, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (904, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1255, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1256, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1277, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1347, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1349, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1353, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1355, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1357, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1361, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (1368, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1387, [('open_storage_with_hand', 'drawer1', 'r_hand'), ('close_storage_with_hand', 'drawer1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1394, [('open_storage_with_hand', 'drawer1', 'l_hand'), ('close_storage_with_hand', 'drawer1', 'l_hand')]), (1395, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1408, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (1417, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (1426, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1460, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1468, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand'), ('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1473, [('cut', 'plastic_paper_bag1', 'knife1'), ('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1'), ('cut', 'drawer1', 'knife1')]), (1478, [('cut', 'cupboard1', 'knife1'), ('cut', 'plastic_paper_bag1', 'knife1')]), (1488, [('open_storage_with_hand', 'drawer1', 'r_hand'), ('close_storage_with_hand', 'drawer1', 'r_hand')]), (1489, [('cut', 'plastic_paper_bag1', 'knife1'), ('cut', 'cupboard1', 'knife1')]), (1497, [('cut', 'counter1', 'knife1')]), (1500, [('cut', 'bread1', 'knife1'), ('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (1518, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (1534, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1540, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1543, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1551, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1560, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1603, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1617, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1620, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1647, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1649, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1658, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1670, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1767, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1773, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1778, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1780, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1783, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1788, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1789, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1791, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (1793, [('cut', 'bread1', 'knife1')]), (1794, [('cut', 'bread1', 'knife1')]), (1795, [('cut', 'plate1', 'knife1'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1802, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand'), ('cut', 'bread1', 'knife1'), ('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1803, [('cut', 'plastic_paper_bag1', 'knife1')]), (1805, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1807, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1821, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1823, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (1826, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (1841, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1873, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1879, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand'), ('cut', 'drawer1', 'knife1'), ('open_storage_with_hand', 'drawer1', 'l_hand'), ('close_storage_with_hand', 'drawer1', 'l_hand'), ('open_storage_with_hand', 'drawer1', 'r_hand'), ('close_storage_with_hand', 'drawer1', 'r_hand')]), (1882, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1883, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1892, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1896, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1899, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1912, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1913, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1923, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1924, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1931, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1933, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1966, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1968, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1983, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1998, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2024, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2025, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2026, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2027, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2030, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2031, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2033, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2047, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2049, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2050, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand'), ('cut', 'plastic_paper_bag1', 'knife1'), ('cut', 'plate1', 'knife1')]), (2051, [('cut', 'bread1', 'knife1')]), (2052, [('cut', 'cuttingboard1', 'knife1')]), (2055, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2063, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2070, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2071, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2072, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2077, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2078, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2082, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2192, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2194, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2197, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2199, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2202, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2204, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2270, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2285, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2296, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2303, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2310, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2362, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2365, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2382, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2384, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2479, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2491, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('cut', 'bread1', 'knife1'), ('cut', 'bread1', 'knife1')]), (2518, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2519, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2520, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2521, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2530, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2568, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2569, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2572, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2573, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2581, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2594, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2600, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2601, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2602, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2603, [('cut', 'bread1', 'knife1')]), (2608, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2609, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2610, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2612, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2614, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2619, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2626, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2627, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2628, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2630, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2631, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2635, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2639, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2640, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2656, [('cut', 'bread1', 'knife1')]), (2657, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2659, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand'), ('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2660, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2661, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2679, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2680, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2681, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2682, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2684, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2693, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2702, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2703, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2705, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2706, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2712, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2724, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2732, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2733, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2744, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2752, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2753, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2771, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2773, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2816, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2821, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2848, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2862, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2908, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2922, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2941, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2942, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2946, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2951, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')])]
        uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), p_a)
    else:
        print("provide valid run_type number")

    G = uct_search.create_nx_graph()
    draw_search_tree_mod.draw_tree_nx(G, 'final')
    print("done")

#TODO make DAG
#TODO make state lookup
#TODO draw graph https://plot.ly/python/tree-plots/

#TODO are nop state really that good?

#http://www.webgraphviz.com/
#insert test.dot there

#kgraphviewer

#look at the test.dot-file in observation_trace_gen

#Hash results of plan rec
#possible to save prelim results and use for next step? probably not.

#TODO make it that unfinished prob folders in ramirez folder are removed automatically

###
#TODO at level 2 (frame no 342), check if the states are correctly expanded --> there are never put_in_hand/put_out_of_hand actions!!!
#TODO: when the search tree has reached max level (no more children to expand) and has done the plan recognition policy already in that state
#then save the PR result for later, if that node is reached again. This would then be similar to a "isTerminal" condition in the
#pseudo code
#TODO: when a goal is reached: then you should not look for it any longer, right?

###TODO: idea: have commands be translated into goals?

#TODO: when there are goals, where one goal is a subset of the other, the most specific goal should be the most probable.
#E.g., clean all containers off table VS clean everything off table --> if up to a point only containers are cleaned,
#then the more specific subgoal should be prefered (maybe via number of reached goal fluents heuristic)

#TODO: the fewer possible acions there are, the better.
#try out different steps:
#lvl 0: use all touch events from bounding boxes
#lvl 1: --"-- from object masks
#lvl 2: use aksoy activity recognition to only have manipulation events, when the touch sequence is right for that specific action
#lvl 3: use more advanced computer vision to instantiate different actions

#TODO : create pddl guidelines for creating pddl domains for this approach
#e.g., which formulations to avoid in order to have "cheap" domains
#how to capture essentials of a domain
#that you can only have at most binary relations

#TODO: incorporate action sequence cost into reward?
#problem: if an action sequence explains a "short" goal as well as a "long" goal, which is preferred?
#solution: probably dont consider action sequence length
#it should be such that, as soon as a goal is plausible, it should be rated highly no matter what

#TODO: DAG is possible to construct and helpful in reducing number of states in search. But in general, with pddl
#domains, there can be loops, e.g., an action plus its reverse action (pick up, put down) this can potentially destroy
#a dag, e.g.: 0 --> 1 <--> 2  as a search tree.
#but we can argue, that an action sequence that loops back can never be a good plan:
#say, there is a sequence pi = pi'+pi'', pi' leads from s_0 to s', and pi'' from s' to s' over some other states, then
#if for all actions c(a) >0, and the goal is s', then of course pi' is sufficient and the better plan to reach s' than pi' + pi''
#so, we need an algorithmmic check if the next action to be added as achild creates a loop in the otherwise DAG.
#if a loop would be created, we know we don't need it.

#DAG TODO:
#have hashtable for state lookup, use state descriptor as hashvalue (set to list, sort list, join by " " --> unique state string)
#store values in edges, rather than in nodes

#TODO MAYBE BIG DRAWBACK:
#say, there is a correct action sequence and each action needs effects of its predecessor in their precondition
#A->B->C
#now lets say, the object tracker somehow doesn't provide object touches that would lead to try out B,
#but the possible actions lead to try out A and then C
#but now, C wont be even tried out, because C is not applicable from A
#although, if there would be an observation sequence including A -> C, then the plan recognition process would
#rediscover B in the solution from initial state to state after action C
#Maybe it is not complete, to filter the possible actions to applicable actions?

#TODO childs 2008, gaudel 2010, saffidine2010 lesen