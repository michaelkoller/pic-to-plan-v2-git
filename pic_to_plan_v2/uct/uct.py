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
            return v.parent.total_reward #TODO can you do it just like that??? avoid plan rec in nop action states, since nothing has changed anyway
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
    run_type = 1
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