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
from datetime import datetime
import random


class UCTTEST:
    def __init__(self):
        self.t_start = time.time()

        self.possible_actions_session = [(i, [("move_left"), ("move_right")]) for i in range(200)]

    def uct_search(self, iteration_limit=None, time_limit=None):
        self.t_start = time.time()
        self. s_0 = str(0)
        self.node_dict = dict()
        self.v_0 = Node(str(self.s_0), None, self.possible_actions_session)
        self.v_0.hash_value = hash(self.v_0.state)
        self.v_0.state_string = self.s_0

        self.e_0 = uct_edge_mod.Edge(None, self.v_0, None, 0)
        self.v_0.in_edges = [self.e_0]
        self.node_dict[self.v_0.state] = self.v_0
        self.n_iter = 0
        self.iteration_limit = iteration_limit if iteration_limit != None else  math.inf
        self.time_limit = time_limit if time_limit != None else math.inf
        self.max_tree_depth = len(self.possible_actions_session) #there are no more observed actions from the bounding box overlaps after that.
                                                    #the tree at max level cannot be expanded further
                                                    #at max level you can only call default policy
                                                    #in DAG, there cannot be a longer path than this
        n_l = Node(str(1), None, self.possible_actions_session) #state, in_edge, possible_actions
        n_l.hash_value = hash(n_l.state)
        n_r = Node(str(-1), None, self.possible_actions_session) #state, in_edge, possible_actions
        n_r.hash_value = hash(n_r.state)
        e_l = uct_edge_mod.Edge(self.v_0, n_l, "move_left", 0)
        e_r = uct_edge_mod.Edge(self.v_0, n_r, "move_right", 0)
        n_l.in_edges = [e_l]
        n_r.in_edges = [e_r]
        self.v_0.untried_children = [(e_l,n_l),(e_r,n_r)]

        avoid_dup_no = 0
        while (time.time()-self.t_start < self.time_limit and self.n_iter < self.iteration_limit):

            if self.n_iter % 10 == 0 and self.n_iter != 0:
                print(datetime.now())
                print("iter", self.n_iter)
                print("avoided duplicate nodes:", avoid_dup_no)
                self.save_dot()
                #pickle.dump(self.node_dict, open( "uct_dat_"+str(self.n_iter)+".p", "wb" ) )

            final_v_l = None
            final_edge_descent_trace = []

            v_l, edge_descent_trace = self.tree_policy(self.v_0)

            while True:
                if v_l.state in self.node_dict: #this state already exists and has a value
                    avoid_dup_no += 1
                    if len(edge_descent_trace) > 0:
                        #check if there is a way from the DESTINATION to ORIGIN (i.e., reverse direction)
                        if self.check_if_reachable(self.node_dict[v_l.state], edge_descent_trace[-1].origin):
                            #AVOIDED LOOP
                            #print("AVOIDED LOOP")
                            for i in range(len(edge_descent_trace[-1].origin.out_edges)):
                                if edge_descent_trace[-1].origin.out_edges[i].destination == v_l:
                                    del edge_descent_trace[-1].origin.out_edges[i]
                            del edge_descent_trace[-1] #delete the loop creating edge from the backup path
                            final_edge_descent_trace += edge_descent_trace
                            delta = final_edge_descent_trace[-1].destination.get_mean_reward()
                            break
                            #TODO so, here I neither insert node nor change edge, should I abort (via continue?) in this case?
                            #No, because then this path will be chosen again, if the rewards aren't changed
                            #this is kind of a terminal node insofar, that the current selected action wont ever become better
                        else:
                            #change edge from current node to already existing node
                            #print(v_l, "already in node dict")
                            edge_descent_trace[-1].destination = self.node_dict[v_l.state]
                            self.node_dict[v_l.state].in_edges.append(edge_descent_trace[-1])
                            final_edge_descent_trace += edge_descent_trace
                            v_l = self.node_dict[v_l.state]
                            v_l, edge_descent_trace = self.tree_policy(v_l)
                else:
                    self.node_dict[v_l.state] = v_l
                    final_edge_descent_trace += edge_descent_trace
                    #delta = int(v_l.state) #default policy
                    #delta = 0.1 + random.random()*0.1 if int(v_l.state) > 0 else  0.05 + random.random()*0.1#default policy
                    #delta = 0
                    delta = int(v_l.state)/100
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
        print(v)
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
                e, v = self.get_best_child_test(v)
                edge_descent_trace.append(e)
        return v, edge_descent_trace #currently never reached, because no useful "is_terminal" definable

    def get_best_child_test(self, v):
        return v.get_best_child()
        #arr = [( ,int(v.out_edges[i].destination.state), i, v.out_edges[i], v.out_edges[i].destination) for i in range(len(v.out_edges))]
        #return max(arr)[2], max(arr)[3]

    def expand(self, v):
        if v.untried_children is None:
            n_l = Node(str(int(v.state)+1), None, self.possible_actions_session)  # state, in_edge, possible_actions
            n_l.hash_value = hash(n_l.state)
            n_r = Node(str(int(v.state)-1), None, self.possible_actions_session)  # state, in_edge, possible_actions
            n_r.hash_value = hash(n_r.state)
            e_l = uct_edge_mod.Edge(v, n_l, "move_left", 0)
            e_r = uct_edge_mod.Edge(v, n_r, "move_right", 0)
            n_l.in_edges = [e_l]
            n_r.in_edges = [e_r]
            v.untried_children = [(e_l, n_l), (e_r, n_r)]
        e_child, v_child = v.choose_untried_action()
        return e_child, v_child

    def default_policy(self, v, observation_trace):
        # #dummy def pol
        return 1
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
            G.add_node(v.state)
            G._node[v.state]['color'] = 'black'
            G._node[v.state]['fillcolor'] = 'white'
            G._node[v.state]["total_reward"] = v.get_total_reward()
            G._node[v.state]["num_visits"] = v.get_visit_count()
            G._node[v.state]["nid"] = v.nid
            G._node[v.state]["state"] = v.state_string
            G._node[v.state]["label"] = "id"+str(v.nid)+ " S:" + str(v.state)+ " " + str(round(v.get_mean_reward(),3) )#+ "\n"+ str(v.state_string)

            for e in v.out_edges:
                #if (v.nid, e.destination.nid) not in G.edges:
                G.add_edge(e.origin.state, e.destination.state)
                G.edges[e.origin.state, e.destination.state]['penwidth'] = 5 * (e.get_mean_reward())
                G.edges[e.origin.state, e.destination.state]['label'] = str(e.action).replace(" ", "\\n")
                G.edges[e.origin.state, e.destination.state]['total_reward'] = str(round(e.total_reward, 2))
                G.edges[e.origin.state, e.destination.state]['num_visits'] = str(round(e.num_visits, 2))
                G.edges[e.origin.state, e.destination.state]['mean_reward'] = str(round(e.get_mean_reward(), 2))
                G.edges[e.origin.state, e.destination.state]['saffidine_mu'] = str(round(e.get_mu(1), 2)) #TODO Attention, parameter should be same d_1 as in algorithm!!!
                get_nx_nodes_a_edges(e.destination, G)
        get_nx_nodes_a_edges(self.v_0, G)
        return G

if __name__ == "__main__":
    uct_search = UCTTEST()
    uct_search.uct_search()
