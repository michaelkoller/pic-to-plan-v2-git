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
import pic_to_plan_v2.uct.uct_edge as uct_edge_mod

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

    def uct_search(self, s_0, iteration_limit=None, time_limit=None):
        """ s_0                 ... initial state
            possible_actions    ... action candidates, [(fram_no, [actions], (...), ...)]
                                    these are not necessarily applicable in a given state.
                                    check with VAL to get applicable actions for a state from possible actions"""
        self.t_start = time.time()
        self. s_0 = s_0
        self.node_dict = dict()
        self.v_0 = Node(self.s_0, None, self.possible_actions_session)
        self.e_0 = uct_edge_mod.Edge(None, self.v_0, None, 0)
        self.v_0.in_edges = [self.e_0]
        self.node_dict[self.v_0.__hash__()] = self.v_0
        self.n_iter = 0
        self.iteration_limit = iteration_limit if iteration_limit != None else  math.inf
        self.time_limit = time_limit if time_limit != None else math.inf
        self.max_tree_depth = len(self.possible_actions_session) #there are no more observed actions from the bounding box overlaps after that.
                                                    #the tree at max level cannot be expanded further
                                                    #at max level you can only call default policy
                                                    #in DAG, there cannot be a longer path than this
        self.v_0.untried_children = self.v_0.call_VAL(self.possible_actions_session[0][1])

        avoid_dup_no = 0
        while (time.time()-self.t_start < self.time_limit and self.n_iter < self.iteration_limit):
            if self.n_iter % 10 == 0 and self.n_iter != 0:
                print("iter", self.n_iter)
                print("avoided duplicate nodes:", avoid_dup_no)
                self.save_dot()
                #pickle.dump(self.node_dict, open( "uct_dat_"+str(self.n_iter)+".p", "wb" ) )

            final_v_l = None
            final_edge_descent_trace = []

            v_l, edge_descent_trace = self.tree_policy(self.v_0)

            while True:
                if v_l.__hash__() in self.node_dict: #this state already exists and has a value
                    avoid_dup_no += 1
                    if len(edge_descent_trace) > 0:
                        #check if there is a way from the DESTINATION to ORIGIN (i.e., reverse direction)
                        if self.check_if_reachable(self.node_dict[v_l.__hash__()], edge_descent_trace[-1].origin):
                            #AVOIDED LOOP
                            del edge_descent_trace[-1] #delete the loop creating edge from the backup path
                            final_v_l = self.node_dict[v_l.__hash__()]
                            final_edge_descent_trace += edge_descent_trace
                            v_l = self.node_dict[v_l.__hash__()]
                            delta = v_l.get_mean_reward()
                            break
                            #TODO so, here I neither insert node nor change edge, should I abort (via continue?) in this case?
                            #No, because then this path will be chosen again, if the rewards aren't changed
                            #this is kind of a terminal node insofar, that the current selected action wont ever become better
                        else:
                            #change edge from current node to already existing node
                            print(v_l, "already in node dict")
                            edge_descent_trace[-1].destination = self.node_dict[v_l.__hash__()]
                            self.node_dict[v_l.__hash__()].in_edges.append(edge_descent_trace[-1])
                            final_edge_descent_trace += edge_descent_trace
                            v_l = self.node_dict[v_l.__hash__()]
                            v_l, edge_descent_trace = self.tree_policy(v_l)
                else:
                    self.node_dict[v_l.__hash__()] = v_l
                    final_edge_descent_trace += edge_descent_trace
                    final_v_l =  v_l
                    delta = self.default_policy(v_l, [e.action for e in final_edge_descent_trace])
                    #attach mu' and n' to this new edge
                    edge_descent_trace[-1].mu_prime = delta
                    edge_descent_trace[-1].n_prime = 1
                    break

            self.backup(final_edge_descent_trace, delta)
            self.n_iter += 1
        #self.v_0.print_subtree()
        self.get_best_path()
        t_stop = time.time()
        processing_time = t_stop - self.t_start
        print("FINISHED", "Frame no:", str(self.possible_actions_session[-1][0]), "Node count:", str(Node.nid))
        print("Processing time:", processing_time, "Video length:", self.possible_actions_session[-1][0] / 30.0, "Realtime factor:",
              self.possible_actions_session[-1][0] / (30.0 * processing_time))
        return 0

    def check_if_reachable(self, from_here, to_here):
        visited = set()
        self.check_if_reachable_aux(from_here, visited)
        return to_here in visited

    def check_if_reachable_aux(self, v, visited):
        visited.add(v)
        for e in v.out_edges:
            self.check_if_reachable_aux(e.destination, visited)

    def save_dot(self):
        G = uct_search.create_nx_graph()
        draw_search_tree_mod.draw_tree_nx(G, self.n_iter)

    def tree_policy(self, v):
        edge_descent_trace = []
        while not v.is_terminal:
            if v.untried_children == [] and v.out_edges == []:
                return v, edge_descent_trace
            elif not v.is_fully_expanded():
                expanded_e, expanded_v = self.expand(v)
                edge_descent_trace.append(expanded_e)
                return expanded_v, edge_descent_trace
            else:
                e, v = v.get_best_child()
                edge_descent_trace.append(e)
        return v, edge_descent_trace #currently never reached, because no useful "is_terminal" definable

    def expand(self, v):
        if v.untried_children is None:
            v.untried_children = v.get_children_from_possible_actions() #call to VAL
        e_child, v_child = v.choose_untried_action()
        return e_child, v_child

    def default_policy(self, v, observation_trace):
        # #dummy def pol
        # return 1
        ###############
        create_pr_instance_mod.create_pr_instance(observation_trace)
        return call_plan_rec_mod.call_plan_rec()

    def backup(self, edge_descent_trace, delta):
        for e in edge_descent_trace[::-1]:
            e.total_reward += delta
            e.num_visits += 1
        self.e_0.total_reward += delta
        self.e_0.num_visits += 1

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
            G._node[v.nid]['color'] = 'black'
            G._node[v.nid]['fillcolor'] = 'white'
            G._node[v.nid]["total_reward"] = v.get_total_reward()
            G._node[v.nid]["num_visits"] = v.get_visit_count()
            G._node[v.nid]["nid"] = v.nid
            G._node[v.nid]["state"] = v.state_string
            G._node[v.nid]["label"] = "id"+str(v.nid)+ " " + str(round(v.get_mean_reward(),3) )#+ "\n"+ str(v.state_string)

            for e in v.out_edges:
                #if (v.nid, e.destination.nid) not in G.edges:
                G.add_edge(e.origin.nid, e.destination.nid)
                G.edges[e.origin.nid, e.destination.nid]['penwidth'] = 5 * (e.get_mean_reward())
                G.edges[e.origin.nid, e.destination.nid]['label'] = str(e.action).replace(" ", "\\n")
                get_nx_nodes_a_edges(e.destination, G)
        get_nx_nodes_a_edges(self.v_0, G)
        return G

if __name__ == "__main__":
    # G = nx.DiGraph()
    # G.add_node(1)
    # G.add_node(2)
    # G.add_node(3)
    # G.add_edge(1,2)
    # G.add_edge(1,3)
    # G.node[2]["test"] = "asdf"
    # G.edges[1,2]['penwidth'] = 3
    # print(G.edges[1,2])
    # print(G.edges)
    # print(G.nodes)
    # print(1 not in G.nodes)
    # exit()
    #run_type = "load"
    #run_type = "test_put"
    run_type = 1
    uct_search = UCTSearch()

    if run_type == 1:
        uct_search.uct_search(copy.deepcopy(uct_search.current_state_set))
    elif run_type == 2:
        cProfile.run("uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), iteration_limit=10)", "profilestats")
        p = pstats.Stats('profilestats')
        # p.strip_dirs().sort_stats('cumulative').print_stats()
        p.sort_stats('cumulative').print_stats()
    elif run_type == 3:
        profiler = cProfile.Profile()
        profiler.run("uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), iteration_limit=10)")
        visualize(profiler.getstats())
        convert(profiler.getstats(), 'profiling_results.kgrind')
    elif run_type == "test_put":
        p_a = [(342, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (372, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (379, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (386, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (438, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (490, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (492, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (524, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (527, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (528, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (531, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (759, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (786, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (787, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (794, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (805, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (819, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (821, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (822, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (831, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (842, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (868, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (892, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (897, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (904, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1255, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1256, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1277, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1347, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1349, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1353, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1355, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1357, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1361, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (1368, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1387, [('open_storage_with_hand', 'drawer1', 'r_hand'), ('close_storage_with_hand', 'drawer1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1394, [('open_storage_with_hand', 'drawer1', 'l_hand'), ('close_storage_with_hand', 'drawer1', 'l_hand')]), (1395, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1408, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (1417, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (1426, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1460, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1468, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand'), ('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1473, [('cut', 'plastic_paper_bag1', 'knife1'), ('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1'), ('cut', 'drawer1', 'knife1')]), (1478, [('cut', 'cupboard1', 'knife1'), ('cut', 'plastic_paper_bag1', 'knife1')]), (1488, [('open_storage_with_hand', 'drawer1', 'r_hand'), ('close_storage_with_hand', 'drawer1', 'r_hand')]), (1489, [('cut', 'plastic_paper_bag1', 'knife1'), ('cut', 'cupboard1', 'knife1')]), (1497, [('cut', 'counter1', 'knife1')]), (1500, [('cut', 'bread1', 'knife1'), ('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')]), (1518, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (1534, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1540, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1543, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1551, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1560, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1603, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1617, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1620, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1647, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1649, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1658, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1670, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1767, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1773, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1778, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1780, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1783, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1788, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (1789, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1791, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (1793, [('cut', 'bread1', 'knife1')]), (1794, [('cut', 'bread1', 'knife1')]), (1795, [('cut', 'plate1', 'knife1'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1802, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand'), ('cut', 'bread1', 'knife1'), ('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1803, [('cut', 'plastic_paper_bag1', 'knife1')]), (1805, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1807, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1821, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1823, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (1826, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (1841, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1873, [('open_storage_with_hand', 'cupboard1', 'l_hand'), ('close_storage_with_hand', 'cupboard1', 'l_hand')]), (1879, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand'), ('cut', 'drawer1', 'knife1'), ('open_storage_with_hand', 'drawer1', 'l_hand'), ('close_storage_with_hand', 'drawer1', 'l_hand'), ('open_storage_with_hand', 'drawer1', 'r_hand'), ('close_storage_with_hand', 'drawer1', 'r_hand')]), (1882, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1883, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1892, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1896, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1899, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1912, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1913, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1923, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1924, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (1931, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1933, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1966, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (1968, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (1983, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (1998, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2024, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2025, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2026, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2027, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2030, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2031, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2033, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2047, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2049, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2050, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand'), ('cut', 'plastic_paper_bag1', 'knife1'), ('cut', 'plate1', 'knife1')]), (2051, [('cut', 'bread1', 'knife1')]), (2052, [('cut', 'cuttingboard1', 'knife1')]), (2055, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2063, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2070, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2071, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2072, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2077, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2078, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2082, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2192, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2194, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2197, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2199, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2202, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2204, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2270, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2285, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2296, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2303, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2310, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2362, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2365, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2382, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2384, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2479, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2491, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('cut', 'bread1', 'knife1'), ('cut', 'bread1', 'knife1')]), (2518, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2519, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2520, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2521, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2530, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2568, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2569, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2572, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2573, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2581, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2594, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2600, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2601, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2602, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2603, [('cut', 'bread1', 'knife1')]), (2608, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2609, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2610, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2612, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2614, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2619, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2626, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2627, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2628, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2630, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2631, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2635, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2639, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2640, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2656, [('cut', 'bread1', 'knife1')]), (2657, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2659, [('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand'), ('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2660, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2661, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2679, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2680, [('put_in_hand', 'plastic_paper_bag1', 'r_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'r_hand')]), (2681, [('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand'), ('put_in_hand', 'bread1', 'r_hand'), ('put_out_of_hand', 'bread1', 'r_hand')]), (2682, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand'), ('put_in_hand', 'plate1', 'r_hand'), ('put_out_of_hand', 'plate1', 'r_hand')]), (2684, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1'), ('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2693, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2702, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2703, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand'), ('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2705, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2706, [('put_in_hand', 'plastic_paper_bag1', 'l_hand'), ('put_out_of_hand', 'plastic_paper_bag1', 'l_hand')]), (2712, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2724, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2732, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2733, [('put_in_hand', 'bread1', 'l_hand'), ('put_out_of_hand', 'bread1', 'l_hand')]), (2744, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2752, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2753, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2771, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2773, [('put_in_hand', 'plate1', 'l_hand'), ('put_out_of_hand', 'plate1', 'l_hand')]), (2816, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2821, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2848, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2862, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2908, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2922, [('put_in_hand', 'knife1', 'l_hand'), ('put_out_of_hand', 'knife1', 'l_hand'), ('cut', 'l_hand', 'knife1')]), (2941, [('put_in_hand', 'cuttingboard1', 'r_hand'), ('put_out_of_hand', 'cuttingboard1', 'r_hand')]), (2942, [('put_in_hand', 'cuttingboard1', 'l_hand'), ('put_out_of_hand', 'cuttingboard1', 'l_hand')]), (2946, [('put_in_hand', 'knife1', 'r_hand'), ('put_out_of_hand', 'knife1', 'r_hand'), ('cut', 'r_hand', 'knife1')]), (2951, [('open_storage_with_hand', 'cupboard1', 'r_hand'), ('close_storage_with_hand', 'cupboard1', 'r_hand')])]
        uct_search.uct_search(copy.deepcopy(uct_search.current_state_set))
    elif run_type == "load":
        node_dict = pickle.load( open( "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/observation_trace_gen/uct_dat_670.p", "rb" ) )
        cur_node_hash = -4603751373260900150
        v = node_dict[cur_node_hash]
        while True:
            best_val, best_edge = -1, None
            for e in v.out_edges:
                if e.get_mean_reward() > best_val:
                    best_val = e.get_mean_reward()
                    best_edge = e
            print(best_edge)
            if best_edge is None:
                break
            v = best_edge.destination

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

#TODO about which possible actions are available at a state:
#again, possible actions is a list [(frame_no, [actions_at_frame_no]), (...), (...), ...]
#assume there are no nop-action, all states are unique in the search DAG
#how to say which possible actions are used to create untried children?
#in a certain node, you must look at all the incoming edges. for each edge you must be able to
#determine, from which index in the possible actions (or frame_no) it comes.
#among the incoming nodes, find the lowest index.
#from this index onward you must potentially add all possible actions with a higher index to this node
#form potential expansion
#explanation: you need at least l actions to reach that state. so it is not possible to even try out
#actions that come before the l-th entry in the possible actions
#so we have a lower bound for the poss act index, together with avoiding duplicate actions, that helps.
#
#BUT is there also an upper bound of the index in possible actions?
#in the end, no. in the final tree, each node must have all possible actions wrt. the min index of edge action
#that leads to it.
#but then there is the number of simulations, too. the added possible action index cannot be higher than the iteration
#number.
#so, possible algorithm: if you're at a node, check if all possible actions between the lower and upper bound are
#passed on to the applicable action generator.
#this means, you need to keep track of two more numbers in each node, representing what has already been added
#then, when you reach a new node, you need to check in the children, if there is a new lower lower bound and if the
#edges wrt. the current iteration number have been added. if not, do add them and then the algorithm will play out each
#unexpanded node once, untill all children of the current node are expanded, right?
#WAIT, there is a better, lower upper bound. you can probably do something with the branching factor:
#if there is a new node, then all of the children will be expanded at least once (algo says so).
#so, if there are untried children left, exand them first. Only if the previous children are all expanded,
#go one index further and add the new untried children of the next entry in possible children

#max possible actions index: keep track of max index and

#branching factor is #distinct actions

#TODO avoid outgoing edges in a node with ther same actions!
#this could potentially happen if you need to insert possible actions many times

#so now i have all unique actions at the root node as edges

#TODO a new and relatively cheap rollout policy, assuming you always have the whole possible actions available:
#create action chain, through all frame_no, choose one or nop. then call VAL, count number of achieved goal fluents
#but in reality you only have all possible actions when observed agent is done with activity, so it's useless...

#TODO have a look at absolute pruning, search tree reuse, breidge burning mcts --> in hearthstone paper


#http://www.webgraphviz.com/ --> zeigt pfeildicke