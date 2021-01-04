import math
import random


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

    def get_saff_p(self, depth):  # payoffs of b(x) (siblings of x plus x)
        return sum([f.get_saff_n(depth) for f in self.get_siblings_plus_self()])

    def get_siblings_plus_self(self):
        return self.origin.out_edges

    def get_children_edges(self):
        return self.destination.out_edges

    def get_best_child_node_plus_edge(self, d_1, d_2, d_3, exploration_value=1.4142135623730951):  # math.sqrt(2)
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
