import math
import random
from graphviz import Digraph

class Node:
    nid = 0
    def __init__(self, state, in_edge):
        self.state = state
        self.untried_children = None
        self.out_edges = []
        self.in_edges = [in_edge]
        self.nid = Node.nid
        Node.nid += 1

    def __repr__(self):
        return "ID " + str(self.nid) + " " + self.state

    def __str__(self):
        return "ID " + str(self.nid) + " " + self.state

    def __hash__(self):
        return self.state.__hash__()

    def is_terminal(self):
        return self.untried_children is not None and len(self.untried_children) == 0 and len(self.out_edges) == 0

    def is_fully_expanded(self):
        return self.untried_children is not None and len(self.untried_children) == 0

    def expand(self):
        if self.untried_children is None:
            self.untried_children = self.get_children_from_possible_actions()
        if self.is_terminal():
            return self, None
        else:
            chosen_child_node, chosen_child_edge = self.untried_children.pop(random.randint(0, len(self.untried_children) - 1))
            self.out_edges.append(chosen_child_edge)
            return chosen_child_node, chosen_child_edge

    def get_children_from_possible_actions(self):
        lowest_pai = self.get_lowest_possible_action_index()
        actions_to_consider = [pa for pa in UCT_Search.possible_actions if pa[0] > lowest_pai]
        new_children = []
        for (pai, action_set) in actions_to_consider:
            for action in action_set:
                new_edge = Edge(self, None, action, pai)  # origin, destination, action, possible_action_index):
                #toy VAL and next state computation:
                new_state = self.state.split(" ")
                if "" in new_state:
                    new_state.remove("")
                if "+" in action:
                    new_atom = action.replace("+","")
                    if new_atom not in new_state:
                        new_state.append(new_atom)
                        new_state = sorted(new_state)
                if "-" in action:
                    remove_atom = action.replace("-","")
                    if remove_atom in new_state:
                        new_state.remove(remove_atom)
                new_state = " ".join(new_state)
                #end toy VAL
                new_node = Node(new_state, new_edge)
                new_edge.destination = new_node
                new_children.append((new_node, new_edge))

        #for duplicate actions take the one with the lower pai
        action_dict = dict()
        for c in new_children:
            if c[1].action not in action_dict:
                action_dict[c[1].action] = c
            elif action_dict[c[1].action][1].possible_action_index > c[1].possible_action_index:
                action_dict[c[1].action] = c
        return list(action_dict.values())

    def get_lowest_possible_action_index(self):
        return min([e.possible_action_index for e in self.in_edges])

    def get_best_child_node_plus_edge(self, exploration_value=1.4142135623730951, d_1=1, d_2=1, d_3=1):  # math.sqrt(2)
        best_value = -math.inf
        best_edges = []
        for e in self.out_edges:
            if e.num_visits == 0:
                edge_value = math.inf
            else:
                # Saffidine, 2010, UCD
                # edge_value = e.get_saff_mu(d_1) + \
                #              exploration_value * math.sqrt(math.log(e.get_saff_p(d_2)) / e.get_saff_n(d_3))
                edge_value = 1
            if edge_value > best_value:
                best_value = edge_value
                best_edges = [e]
            elif edge_value == best_value:
                best_edges.append(e)
        chosen_edge = random.choice(best_edges)
        return chosen_edge.destination, chosen_edge

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
        self.mu_prime = 0
        self.n_prime = 0

    def __repr__(self):
        return "ID " + str(self.eid) + " " + str(self.action)

    def __str__(self):
        return "ID " + str(self.eid) + " " + str(self.action)


    def get_normal_mean_reward(self):
        return self.total_reward / self.num_visits if self.num_visits > 0 else math.inf

    def get_saff_mu(self):
        pass

    def get_saff_n(self):
        pass

    def get_saff_p(self):
        pass


class UCT_Search:
    possible_actions = [(1, ["A+", "B+"]), (2, ["A+", "B+"]), (3, ["B-"]), (4, ["C+"])]
    #possible_actions = [(1, ["A+", "B+", "C+", "D+"]), (2, ["A+", "B+", "C+"]), (3, ["A+", "B+"]), (4, ["A+"])]
    #possible_actions = [(1, ["A+"]), (2, ["B+"]), (3, ["C+"]), (4, ["D+"])]
    #possible_actions = [(1, ["A+"]), (2, ["B+"]), (3, ["A-"]), (4, ["C+"]), (5, ["B-"]), (6, ["D+"]), (7, ["C-"]), (8, ["D-"])]
    d_1 = 1
    d_2 = 1
    d_3 = 1

    def __init__(self, initial_state):
        self.e_0 = Edge(None, None, None, -1)
        self.n_0 = Node(initial_state, self.e_0)
        self.e_0.destination = self.n_0

        self.node_dict = dict()
        self.node_dict[self.n_0.__hash__()] = self.n_0
        self.edge_dict = dict()
        self.edge_dict[self.e_0.action] = self.e_0
        self.n_iter = 0
        self.n_iter_limit = 1000

    def search(self):

        while self.n_iter < self.n_iter_limit:
            #start new descent
            edge_descent_trace = []
            tp_result_node, tp_result_edge_trace = self.tree_policy(self.n_0)
            while True:
                if tp_result_node.__hash__() in self.node_dict: #state already in DAG
                    if len(tp_result_edge_trace) > 0:
                        #check for loop possibility
                        if self.check_if_reachable(self.node_dict[tp_result_node.__hash__()], tp_result_edge_trace[-1].origin):
                            #print("Detected loop creating action", tp_result_edge_trace[-1].origin, "-->", tp_result_edge_trace[-1], "-->", tp_result_node)
                            #AVOIDED LOOP
                            for i in range(len(tp_result_edge_trace[-1].origin.out_edges)):
                                if tp_result_edge_trace[-1].origin.out_edges[i].destination == tp_result_node:
                                    del tp_result_edge_trace[-1].origin.out_edges[i]
                            del tp_result_edge_trace[-1] #delete the loop creating edge from the backup path
                            edge_descent_trace += tp_result_edge_trace
                            #BACKUP OR NO?
                            break
                        else:
                            #print("Detected DAG case", tp_result_edge_trace[-1].origin, "-->", tp_result_edge_trace[-1], "-->", tp_result_node)
                            tp_result_edge_trace[-1].destination = self.node_dict[tp_result_node.__hash__()]
                            self.node_dict[tp_result_node.__hash__()].in_edges.append(tp_result_edge_trace[-1])
                            edge_descent_trace += tp_result_edge_trace
                            tp_result_node = self.node_dict[tp_result_node.__hash__()]
                            tp_result_node, tp_result_edge_trace = self.tree_policy(tp_result_node)
                    else:
                        break
                else:
                    #print("Detected new node", tp_result_edge_trace[-1].origin, "-->", tp_result_edge_trace[-1], "-->", tp_result_node)
                    self.node_dict[tp_result_node.__hash__()] = tp_result_node
                    edge_descent_trace += tp_result_edge_trace
                    default_policy_result_value = self.default_policy() #TODO the mu_prime, n_prime should really be updated in the default_policy() --> also, then the mu_prime is just the saved value from the plan rec call
                    edge_descent_trace[-1].mu_prime = default_policy_result_value
                    edge_descent_trace[-1].n_prime = 1
                    break

            if len(edge_descent_trace) > 0:
                self.backup(edge_descent_trace, self.default_policy()) #TODO check in default policy, with the input of edge_descent_trace, if this is a case, where a loop has been avoided, then only backup from that state, if it is really a terminal state
            self.n_iter += 1
        print("Limit reached", self.n_iter, "/", self.n_iter_limit)

    def tree_policy(self, tp_orig_node):
        tp_result_edge_trace = []
        tp_result_node = tp_orig_node

        while not tp_result_node.is_terminal():
            if not tp_result_node.is_fully_expanded():
                expanded_n, expanded_e = tp_result_node.expand()
                if expanded_e is not None:
                    tp_result_edge_trace.append(expanded_e)
                return expanded_n, tp_result_edge_trace
            else:
                tp_result_node, e = tp_result_node.get_best_child_node_plus_edge()
                tp_result_edge_trace.append(e)
        return tp_result_node, tp_result_edge_trace

    def default_policy(self):
        return 1

    def backup(self, edge_descent_trace, delta):
        for e in edge_descent_trace:
            e.num_visits += 1
            e.total_reward += delta

    def check_if_reachable(self, from_here, to_here):
        visited = set()
        self.check_if_reachable_aux(from_here, visited)
        return to_here in visited

    def check_if_reachable_aux(self, v, visited):
        visited.add(v)
        for e in v.out_edges:
            self.check_if_reachable_aux(e.destination, visited)

    def viz(self, viz_name):
        dot = Digraph(comment=viz_name)
        nd = dict()
        ed = dict()
        self.viz_add_aux(dot, self.n_0, nd, ed)
        dot.render(viz_name+".gv", view=True)
        return dot

    def viz_add_aux(self, dot, node, nd, ed):
        if node.nid not in nd:
            nd[node.nid] = node
            if node.untried_children is None:
                untried_children_status = "\nn.e."
            else:
                untried_children_status = "" if len(node.untried_children) == 0 else "\nutchild"+str(len(node.untried_children))
            dot.node(node.state, node.state + untried_children_status)
        for e in node.out_edges:
            if e.eid not in ed:
                ed[e.eid] = e
                dot.edge(node.state, e.destination.state, e.action + "\nn:" + str(e.num_visits))
                self.viz_add_aux(dot, e.destination, nd, ed)


if __name__ == "__main__":
    uct_search = UCT_Search("")
    uct_search.search()
    uct_search.viz("test-viz")