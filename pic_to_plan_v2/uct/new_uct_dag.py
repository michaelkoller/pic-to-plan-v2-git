import math
import random
from graphviz import Digraph
import time
import re
import pickle
import pic_to_plan_v2.observation_trace_gen.parsed_proplem as parsed_problem_mod
import pic_to_plan_v2.observation_trace_gen.video_annotation as video_annotation_mod
import os
import copy
import pic_to_plan_v2.observation_trace_gen.create_pr_instance as create_pr_instance_mod
import pic_to_plan_v2.observation_trace_gen.call_plan_rec as call_plan_rec_mod
import multiprocessing as mp
from datetime import datetime
import collections
import pic_to_plan_v2.observation_trace_gen.save_deepcopy as save_deepcopy_mod


d_1 = -1
d_2 = 0
d_3 = 0

class Node:
    nid = 0
    re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)")

    def __init__(self, state, in_edge, possible_actions_session, domain_inserted_predicates_path, instance_parsed_objects_path):
        self.state = state
        self.state_string = " ".join(sorted(list(self.state)))
        self.hash_value = self.state_string.__hash__()
        self.untried_children = None
        self.out_edges = []
        self.in_edges = [in_edge]
        self.nid = Node.nid
        Node.nid += 1
        self.mu_prime = None
        self.n_prime = None
        self.possible_actions = possible_actions_session
        self.domain_inserted_predicates_path = domain_inserted_predicates_path
        self.instance_parsed_objects_path = instance_parsed_objects_path
        self.detailed_pr_vals = []
        self.do_dead_state_check = True

    def __repr__(self):
        return "ID " + str(self.nid) + " " + self.state_string

    def __str__(self):
        return "ID " + str(self.nid) + " " + self.state_string

    def __hash__(self):
        return self.hash_value

    def is_terminal(self):
        return self.untried_children is not None and len(self.untried_children) == 0 and len(self.out_edges) == 0

    def is_fully_expanded(self):
        return self.untried_children is not None and len(self.untried_children) == 0

    def expand(self):
        if self.untried_children is None:
            self.untried_children = self.get_children_from_possible_actions()
        if self.is_terminal():
            print("TRIED TO EXPAND TERMINAL NODE")
            return self, None
        else:
            chosen_child_node, chosen_child_edge = self.untried_children.pop(random.randint(0, len(self.untried_children) - 1))
            self.out_edges.append(chosen_child_edge)
            return chosen_child_node, chosen_child_edge

    def get_children_from_possible_actions(self):
        pos_act_children = self.call_VAL()
        return pos_act_children

    def call_VAL(self): #not using n_iter. it's just a call to get_min_in_edge
        current_plan_path_string = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plans/current_sas_plan_try_"

        try_action_strings = []
        plan_file_names = []
        pos_act_indices = []
        for pos_act_index in range(self.get_lowest_possible_action_index(), len(self.possible_actions)):
            for i, try_action in enumerate(self.possible_actions[pos_act_index][1]):
                try_action_string = "(" + " ".join(try_action) + ")"    #create the plan for the action to try
                if try_action_string not in try_action_strings:
                    try_action_strings.append(try_action_string)
                    plan_file_names.append(current_plan_path_string+str(pos_act_index)+"_"+str(i))
                    pos_act_indices.append(pos_act_index)
                    f = open(plan_file_names[-1], "w")
                    f.write(try_action_string + "\n;cost = 1 (unit cost)")
                    f.close()
        current_state_string = " ".join(self.state)
        template_instance = open(self.instance_parsed_objects_path.replace(".pddl", "-insert-init.pddl"), "r")
        template_instance_string = "".join(template_instance.readlines())
        parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
        f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl", "w")
        f.write(parsed_template_instance_string)
        f.close()
        cmd = '/home/mk/Planning/VAL/validate -v ' + self.domain_inserted_predicates_path + \
                        ' /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl ' \
              + " ".join(plan_file_names) + \
              ' > /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt'
        os.system(cmd)
        plan_val_output = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt", "r")
        plan_val_output_joined = "".join(plan_val_output.readlines())
        new_state_sets = []
        plan_val_output = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt", "r") #TODO superfluous open, but readlines changes the iterator...
        new_atom_added_list = []
        for line in plan_val_output:
            if "Checking plan" in line:
                new_atom_added_list.append(False)
                new_state_sets.append(copy.deepcopy(self.state))
            elif "Deleting" in line:
                new_atom_added_list[-1] = True
                m = Node.re_compiled.search(line) #actually not really the correct regex, becaus (asdf asdf) (asdf asdf) will be recognized as 1 occurance, but here only ever 1 atom per line appears
                atom_to_delete = m.group(0)
                if atom_to_delete in new_state_sets[-1]:
                    new_state_sets[-1].remove(atom_to_delete)
            elif "Adding" in line:
                new_atom_added_list[-1] = True
                m = Node.re_compiled.search(line)
                atom_to_add = m.group(0)
                if atom_to_add not in new_state_sets[-1]:
                    new_state_sets[-1].add(atom_to_add)
        children = []
        for i, new_state in enumerate(new_state_sets):
            if new_atom_added_list[i]: # and sorted_new_state_string not in state_string_to_node_id_dict.keys(): #new atom short circuits logical expression
                new_edge = Edge(self, None, try_action_strings[i], pos_act_indices[i]) #origin, destination, action, possible_action_index):
                new_node = Node(new_state, new_edge, self.possible_actions, self.domain_inserted_predicates_path, self.instance_parsed_objects_path) #state, in_edge, possible_actions):
                new_edge.destination = new_node
                children.append((new_node, new_edge))
        return children

    def get_lowest_possible_action_index(self):
        return min([e.possible_action_index for e in self.in_edges])

class Edge:
    eid = 0
    def __init__(self, origin, destination, action, possible_action_index):
        self.origin = origin
        self.destination = destination
        self.action = action
        self.possible_action_index = possible_action_index
        self.eid = Edge.eid
        Edge.eid += 1
        self.num_visits = 0
        self.total_reward = 0.0
        self.mu_prime = None
        self.n_prime = None

    def __repr__(self):
        return "ID " + str(self.eid) + " " + str(self.action)

    def __str__(self):
        return "ID " + str(self.eid) + " " + str(self.action)


    def get_normal_mean_reward(self):
        return self.total_reward / self.num_visits if self.num_visits > 0 else math.inf

    def get_saff_mu(self, depth):
        if depth == 0:
            return self.get_normal_mean_reward()
        else:
            return ((self.mu_prime * self.n_prime) + sum(
                [f.get_saff_mu(depth - 1) * f.num_visits for f in self.get_children_edges()])) / \
                   (self.n_prime + sum([g.num_visits for g in self.get_children_edges()]))

    def get_saff_n(self, depth):
        if depth == 0:
            return self.num_visits
        else:
            return self.n_prime + sum([f.get_saff_n(depth - 1) for f in self.get_children_edges()])

    def get_saff_p(self, depth): #payoffs of b(x) (siblings of x plus x)
        return sum([f.get_saff_n(depth) for f in self.get_siblings_plus_self()])

    def get_siblings_plus_self(self):
        return self.origin.out_edges

    def get_children_edges(self):
        return self.destination.out_edges

    def get_best_child_node_plus_edge(self, exploration_value=1.4142135623730951, d_1=d_1, d_2=d_2, d_3=d_3):  # math.sqrt(2)
        best_value = -math.inf
        best_edges = []
        for e in self.destination.out_edges:
            if e.num_visits == 0:
                edge_value = math.inf
            else:
                # Saffidine, 2010, UCD
                edge_value = e.get_saff_mu(d_1) + \
                              exploration_value * math.sqrt(math.log(e.get_saff_p(d_2)) / e.get_saff_n(d_3))
            if edge_value > best_value:
                best_value = edge_value
                best_edges = [e]
            elif edge_value == best_value:
                best_edges.append(e)
        chosen_edge = random.choice(best_edges)
        return chosen_edge.destination, chosen_edge


class UCT_Search:
    def __init__(self, domain_inserted_predicates_path, instance_parsed_objects_path, session_name, ontology_path, \
                 save_after_X_iterations, experiment_name, current_results_dir, goal_path, possible_actions_percentage):
        self.t_start = time.time()
        self.n_iter = 0
        self.save_after_X_iterations = save_after_X_iterations
        self.experiment_name = experiment_name
        self.current_results_dir = current_results_dir
        # compile re for later use
        self.re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)")
        self.domain_inserted_predicates_path = domain_inserted_predicates_path
        self.instance_parsed_objects_path = instance_parsed_objects_path
        self.ontology_path = ontology_path
        self.possible_actions_percentage = possible_actions_percentage
        self.goal_path = goal_path
        self.no_goals = 0
        self.goals = []
        self.goal_sets = []
        with open(self.goal_path) as f:
            for i, l in enumerate(f):
                #goal string
                self.goals.append(l)
                #goal set
                found_atoms_list = Node.re_compiled.findall(l)
                g_s = set()
                for a in found_atoms_list:
                    g_s.add(a)
                self.goal_sets.append(g_s)
            self.no_goals = i + 1

        self.my_parsed_problem = parsed_problem_mod.ParsedPDDLProblem(domain_inserted_predicates_path,
                                                                      instance_parsed_objects_path, ontology_path)

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

        self.session_name = session_name
        print(self.session_name)
        self.touch_events = pickle.load(open(
            "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/overlap_detections/touch_events_" + self.session_name + ".p",
            "rb"))
        self.possible_actions_session_full_length = pickle.load(open(
            "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_" + self.session_name + ".p",
            "rb"))
        self.possible_actions_session = self.possible_actions_session_full_length[0:int(len(self.possible_actions_session_full_length)*self.possible_actions_percentage + 0.5)]

        # get current state from parsed problem
        self.current_state_FD = self.my_parsed_problem.parsed_problem_FD.init
        self.current_state_set = set()
        for atom in self.current_state_FD:
            if atom.predicate != "=" and self.my_parsed_problem.onto[
                atom.predicate] is None:
                s = "(" + str(atom.predicate) + " " + " ".join(atom.args) + ")"
                self.current_state_set.add(s)
#####



    def search(self, s_0, iteration_limit=None, time_limit=None):

        self.e_0 = Edge(None, None, None, -1)
        self.n_0 = Node(s_0, self.e_0, self.possible_actions_session, self.domain_inserted_predicates_path, self.instance_parsed_objects_path)
        self.e_0.destination = self.n_0

        self.node_dict = dict()
        self.node_dict[self.n_0.__hash__()] = self.n_0
        self.n_iter = 0
        self.n_iter_limit = iteration_limit if iteration_limit != None else  math.inf
        self.time_limit = time_limit if time_limit != None else math.inf

        while self.n_iter < self.n_iter_limit and time.time() - self.t_start < self.time_limit:
            if self.n_iter % self.save_after_X_iterations == 0:
                print("IT", self.n_iter)
                self.viz("viz-"+str(self.n_iter))
                self.save_nodes_and_edges()
                self.save_root_node()

            #start new descent
            edge_descent_trace = []
            tp_result_node, tp_result_edge_trace = self.tree_policy(self.e_0)
            while True:
                if tp_result_node.__hash__() in self.node_dict: #state already in DAG
                    if len(tp_result_edge_trace) > 1:
                        #check for loop possibility
                        if self.check_if_reachable(self.node_dict[tp_result_node.__hash__()], tp_result_edge_trace[-1].origin):
                            #print("Detected loop creating action", tp_result_edge_trace[-1].origin, "-->", tp_result_edge_trace[-1], "-->", tp_result_node)
                            #AVOIDED LOOP
                            for i in range(len(tp_result_edge_trace[-1].origin.out_edges)):
                                if tp_result_edge_trace[-1].origin.out_edges[i].destination == tp_result_node:
                                    del tp_result_edge_trace[-1].origin.out_edges[i]
                            del tp_result_edge_trace[-1] #delete the loop creating edge from the backup path
                            edge_descent_trace += tp_result_edge_trace
                            break
                        else:
                            #print("Detected DAG case", tp_result_edge_trace[-1].origin, "-->", tp_result_edge_trace[-1], "-->", tp_result_node)
                            tp_result_edge_trace[-1].destination = self.node_dict[tp_result_node.__hash__()]
                            self.node_dict[tp_result_node.__hash__()].in_edges.append(tp_result_edge_trace[-1])
                            edge_descent_trace += tp_result_edge_trace
                            tp_result_node, tp_result_edge_trace = self.tree_policy(edge_descent_trace[-1])
                    else:
                        break
                else:
                    #print("Detected new node", tp_result_edge_trace[-1].origin, "-->", tp_result_edge_trace[-1], "-->", tp_result_node)
                    self.node_dict[tp_result_node.__hash__()] = tp_result_node
                    edge_descent_trace += tp_result_edge_trace
                    break

            if len(edge_descent_trace) > 1:
                if edge_descent_trace[-1].destination.mu_prime is None:
                    default_policy_result_value = self.default_policy(edge_descent_trace)
                    edge_descent_trace[-1].destination.mu_prime = default_policy_result_value
                    edge_descent_trace[-1].destination.n_prime = 1.0
                if edge_descent_trace[-1].mu_prime is None:
                    edge_descent_trace[-1].mu_prime = edge_descent_trace[-1].destination.mu_prime
                    edge_descent_trace[-1].n_prime = edge_descent_trace[-1].destination.n_prime
                    self.backup(edge_descent_trace, edge_descent_trace[-1].mu_prime)
                elif edge_descent_trace[-1].destination.is_terminal():
                    #found a dead state (if the dest node has still untried children left, you just remove a loop creating edge during this single descent.
                    #but if the state is really dead, the terminal value should be backpropagated
                    self.backup(edge_descent_trace, edge_descent_trace[-1].mu_prime)
                for e in edge_descent_trace[:-1]:
                    if e.mu_prime is None:
                        e.mu_prime = e.destination.mu_prime
                        e.n_prime = 1
            self.n_iter += 1
        print("Limit reached", self.n_iter, "/", self.n_iter_limit)

    def tree_policy(self, tp_orig_edge):
        tp_result_edge_trace = [tp_orig_edge]
        tp_result_node = tp_orig_edge.destination

        while not tp_result_node.is_terminal():
            if not tp_result_node.is_fully_expanded():
                expanded_n, expanded_e = tp_result_node.expand()
                if expanded_e is not None:
                    tp_result_edge_trace.append(expanded_e)
                return expanded_n, tp_result_edge_trace
            else:
                tp_result_node, e = tp_result_edge_trace[-1].get_best_child_node_plus_edge()
                tp_result_edge_trace.append(e)
        return tp_result_node, tp_result_edge_trace

    def default_policy(self, observation_trace):
        useable_cores = 10

        observation_traces = [observation_trace] #the 0-th item in the list is the original found trace, now add more traces of untried siblings

        #look for additional untried children that are not yet in the node dict --> i.e., nodes for which PR definitely needs to be called
        parent = observation_trace[-1].origin
        for i, (child_node, child_edge) in enumerate(parent.untried_children):
            if i >= useable_cores -1:
                break
            print(child_node, child_edge)
            if child_node.__hash__() not in self.node_dict:
                self.node_dict[child_node.__hash__()] = child_node
                observation_trace[-1].origin.out_edges.append(child_edge)
                observation_trace[-1].origin.untried_children[i] = None
                observation_traces.append(save_deepcopy_mod.save_deepcopy_edges(observation_trace)[:-1] + [child_edge])
        for x in range(observation_trace[-1].origin.untried_children.count(None)):
            observation_trace[-1].origin.untried_children.remove(None)

        #determine no remaining useable cores
        no_unused_cores = useable_cores - len(observation_traces)
        no_first_evaluations = len(observation_traces)
        random_choice_lengths = [i for i in range(2, len(observation_trace))] #2, because first edge is from dummy node (TODO check)
        chosen_obs_lengths = []
        for i in range(no_unused_cores):
            if len(random_choice_lengths) == 0:
                break
            rand_choice = random.choice(random_choice_lengths)
            chosen_obs_lengths.append(rand_choice)
            random_choice_lengths.remove(rand_choice)
            observation_traces.append(save_deepcopy_mod.save_deepcopy_edges(observation_trace)[0:rand_choice])

        #create additional traces + lookup table to know where to put results. use chosen_obs_lengths for that
        #after running the pr calls, update the reevaluated nodes as follows:
        #if the new n' result is lower than the old one, change it, and for all parent nodes
        #in the trace, substract n * old_result and add n * new_result
        #but this is not correct for DAGs, because the node could be reached on another path than the trace...

        archive_path = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/"
        for i in range(len(observation_traces)):
            archive_name = "pr_instance_" + str(i)
            create_pr_instance_mod.create_pr_instance([e.action for e in observation_traces[i][1:]], # exclude the first item, becaus it is the dummy root edge
                                                  self.domain_inserted_predicates_path,
                                                  self.instance_parsed_objects_path, self.goal_path, archive_path,
                                                  archive_name)

        return_array = mp.Array('f', [-1.0 for _ in range(len(observation_traces))])
        #3: pr-prob value, cost of satisfied obs, cost of unsatisfied obs
        detailed_pr_vals_array = mp.Array('f', [-1.0 for _ in range(len(observation_traces)*self.no_goals*3)])
        processes = [mp.Process(target=call_plan_rec_mod.call_plan_rec, args=(j, return_array, detailed_pr_vals_array)) for j in
                     range(len(observation_traces))]

        if False:  # possible to return dummy values here
            return_values = [1 for i in range(len(observation_traces))]
        else:
            for p in processes:
                p.start()
            for p in processes:
                p.join()
            return_values = [return_array[i] for i in range(len(observation_traces))]
        detailed_pr_vals = [detailed_pr_vals_array[i] for i in range(len(detailed_pr_vals_array))]

        for i in range(len(observation_traces)): #insert detailed PR values for all nodes (including 0-th)
            if i < no_first_evaluations:
                observation_traces[i][-1].destination.detailed_pr_vals = []
                for j in range(self.no_goals):
                    ind = (i*self.no_goals*3) + (j*3)
                    a = [self.goals[j], detailed_pr_vals[ind], detailed_pr_vals[ind +1], detailed_pr_vals[ind + 2]] #which goal, prob value, cost O, cost not O (?)
                    observation_traces[i][-1].destination.detailed_pr_vals.append(a)
            else: # for reevaluation nodes
                for j in range(self.no_goals):
                    ind = (i*self.no_goals*3) + (j*3)
                    a = [self.goals[j], detailed_pr_vals[ind], detailed_pr_vals[ind +1], detailed_pr_vals[ind + 2]]
                    if a[3] < observation_traces[i][-1].destination.detailed_pr_vals[j][3]:
                        observation_traces[i][-1].destination.detailed_pr_vals[j][1] = a[1]
                        observation_traces[i][-1].destination.detailed_pr_vals[j][2] = a[2]
                        observation_traces[i][-1].destination.detailed_pr_vals[j][3] = a[3]

        print("DET VALS", detailed_pr_vals)

        for i in range(1, len(observation_traces)): # do graph updates for all new nodes except the original first one here in the def pol
            if i < no_first_evaluations:
                observation_traces[i][-1].destination.mu_prime = return_values[i]
                observation_traces[i][-1].destination.n_prime = 1.0
                observation_traces[i][-1].mu_prime = observation_traces[i][-1].destination.mu_prime
                observation_traces[i][-1].n_prime = observation_traces[i][-1].destination.n_prime
                self.backup(observation_traces[i], observation_traces[i][-1].mu_prime)
            else: #for reevaluation nodes
                if return_values[i] < observation_traces[i][-1].destination.mu_prime:
                    observation_traces[i][-1].destination.mu_prime = return_values[i]
                    observation_traces[i][-1].mu_prime = observation_traces[i][-1].destination.mu_prime
                    #TODO no backup of the reevaluated nodes yet
        return return_values[0]

    def backup(self, edge_descent_trace, delta):
        for e in edge_descent_trace:
            e.num_visits += 1
            e.total_reward += delta
        #even if the state will be removed, the reward is backuped once, before that state is removed
        self.dead_state_removal(edge_descent_trace[-1].destination)

    def check_if_reachable(self, from_here, to_here):
        visited = set()
        self.check_if_reachable_aux(from_here, visited)
        return to_here in visited

    def check_if_reachable_aux(self, v, visited):
        visited.add(v)
        for e in v.out_edges:
            self.check_if_reachable_aux(e.destination, visited)

    def dead_state_removal(self, node):
        if node.do_dead_state_check and node.is_terminal():
            print(node)
            state_satisfies_goal = False
            for g_s in self.goal_sets:
                if g_s.issubset(node.state):
                    state_satisfies_goal = True
            if state_satisfies_goal == True:
                node.do_dead_state_check = False
            else:
                for in_e in node.in_edges:
                    print(in_e)
                    if in_e in in_e.origin.out_edges:
                        in_e.origin.out_edges.remove(in_e)

    def viz(self, viz_name):
        dot = Digraph(comment=viz_name)
        nd = dict()
        ed = dict()
        self.viz_add_aux(dot, self.n_0, nd, ed)
        date = str(datetime.now())
        dot.render(self.current_results_dir+"/"+viz_name+"_"+str(self.n_iter)+".gv", view=False)

        return dot

    def viz_add_aux(self, dot, node, nd, ed):
        if node.nid not in nd:
            nd[node.nid] = node
            if node.untried_children is None:
                untried_children_status = "\nn.e."
            else:
                untried_children_status = "" if len(node.untried_children) == 0 else "\nutchild"+str(len(node.untried_children))
            dot.node(node.state_string, node.state_string + untried_children_status)
        for e in node.out_edges:
            if e.eid not in ed:
                ed[e.eid] = e
                dot.edge(node.state_string, e.destination.state_string, e.action + "\nsmu:" + str(round(e.get_saff_mu(d_1),3)) + "\nmean:" + str(round(e.get_normal_mean_reward(),3)) + "\nn:" + str(e.num_visits) + "\nmu':" + str(round(e.mu_prime, 3)) + "\nn':" + str(e.n_prime))
                self.viz_add_aux(dot, e.destination, nd, ed)

    def save_nodes_and_edges(self):
        new_node_dict = collections.defaultdict(list)
        new_in_edge_dict = collections.defaultdict(list)
        new_out_edge_dict = collections.defaultdict(list)
        self.save_nodes_and_edges_aux(new_node_dict, new_in_edge_dict, new_out_edge_dict, self.n_0)
        pickle.dump(new_node_dict, open(self.current_results_dir+"/node_dict_"+str(self.experiment_name)+"_"+str(self.n_iter)+".p", "wb"))
        pickle.dump(new_in_edge_dict, open(self.current_results_dir+"/in_edge_dict_"+str(self.experiment_name)+"_"+str(self.n_iter)+".p", "wb"))
        pickle.dump(new_out_edge_dict, open(self.current_results_dir+"/out_edge_dict_"+str(self.experiment_name)+"_"+str(self.n_iter)+".p", "wb"))

    def save_nodes_and_edges_aux(self, new_node_dict, new_in_edge_dict, new_out_edge_dict, current_node):
        current_node_copy = save_deepcopy_mod.save_deepcopy_node(current_node)
        current_node_copy.out_edges = None
        current_node_copy.in_edges = None
        new_node_dict[current_node_copy.state_string] = current_node_copy
        if current_node.out_edges is not None:
            for i in range(len(current_node.out_edges)):
                e = save_deepcopy_mod.save_deepcopy_edge(current_node.out_edges[i])
                e.saved_saff_mu_val = current_node.out_edges[i].get_saff_mu(-1)
                e.origin = None
                e.destination = None
                new_out_edge_dict[current_node_copy.state_string].append([current_node.out_edges[i].destination.state_string, e])
                new_in_edge_dict[current_node.out_edges[i].destination.state_string].append([current_node_copy.state_string, e])

                self.save_nodes_and_edges_aux(new_node_dict, new_in_edge_dict, new_out_edge_dict, current_node.out_edges[i].destination)

    def save_root_node(self):
        pickle.dump(self.n_0, open(self.current_results_dir+"/root_node_"+str(self.experiment_name)+"_"+str(self.n_iter)+".p", "wb"))

    def save_UCT_DAG(self):
        problem_swap = self.my_parsed_problem
        self.my_parsed_problem = None
        n_0_swap = self.n_0
        self.n_0 = None
        pickle.dump(self, open(self.current_results_dir+"/uct_dag_"+str(self.experiment_name)+"_"+str(self.n_iter)+".p", "wb"))
        self.my_parsed_problem = problem_swap
        self.n_0 = n_0_swap

if __name__ == "__main__":
    uct_search = UCT_Search("")
    uct_search.search()
    uct_search.viz("viz-" + str(uct_search.n_iter))
    uct_search.save_nodes_and_edges()
    uct_search.save_root_node()
    print("Finished")