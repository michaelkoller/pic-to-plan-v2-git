import math
import random

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

    def is_terminal(self):
        return self.untried_children is not None and len(self.untried_children) == 0 and len(self.out_edges) == 0

    def is_fully_expanded(self):
        return self.untried_children is not None and len(self.untried_children) == 0

    def expand(self):
        if self.untried_children is None:
            self.untried_children = self.get_children_from_possible_actions()
        chosen_child_node, chosen_child_edge = self.untried_children.pop(random.randint(0, len(self.untried_children) - 1))
        self.out_edges.append(chosen_child_edge[1])
        return chosen_child_node, chosen_child_edge

    def get_children_from_possible_actions(self):
        lowest_pai = self.get_lowest_possible_action_index()

        return [pa[1] for pa in UCT_Search.possible_actions if pa[0] >= lowest_pai]

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
                edge_value = e.get_saff_mu(d_1) + \
                             exploration_value * math.sqrt(math.log(e.get_saff_p(d_2)) / e.get_saff_n(d_3))
            if edge_value > best_value:
                best_value = edge_value
                best_edges = [e]
            elif edge_value == best_value:
                best_edges.append(e)
        chosen_edge = random.choice(best_edges)
        # print("in get best child, d-vals:", d_1, d_2, d_3, best_value)
        return chosen_edge, chosen_edge.destination

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
    possible_actions = [(1, ["A+"]), (2, ["B+"]), (3, ["C+"]), (4, ["D+"])]
    d_1 = 1
    d_2 = 1
    d_3 = 1

    def __init__(self, initial_state):
        self.e_0 = Edge(None, None, None, -1)
        self.n_0 = Node(initial_state, self.e_0)
        self.e_0.destination = self.n_0

        self.node_dict = dict()
        self.node_dict[self.n_0.state] = self.n_0
        self.edge_dict = dict()
        self.edge_dict[self.e_0.action] = self.e_0
        self.n_iter = 0
        self.n_iter_limit = 100

    def search(self):

        while self.n_iter < self.n_iter_limit:
            #start new descent
            edge_descent_trace = []
            tp_result_node, tp_result_edge_trace = self.tree_policy(self.n_0)

    def tree_policy(self, tp_orig_node):
        tp_result_edge_trace = []
        tp_result_node = tp_orig_node

        while not tp_result_node.is_terminal():
            if not tp_result_node.is_fully_expanded():
                expanded_n, expanded_e = tp_result_node.expand()
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
            e.total_reward += 1

if __name__ == "__main__":
    uct_search = UCT_Search("")
    uct_search.search()