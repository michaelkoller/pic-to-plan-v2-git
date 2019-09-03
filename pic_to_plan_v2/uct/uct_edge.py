import math
import random
import os
import re
import copy
import time

class Edge:
    eid = 0
    re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)") #TODO pass it down from uct_search instead of setting it here

    def __init__(self, origin, destination, action, possible_action_index):
        self.action = action
        self.origin = origin
        self.destination = destination
        self.num_visits = 1 #TODO Achtung, hack, sollte eigentlich mit 0 funktionieren!!!!!!!!!!!!!
        self.n_prime = 1
        self.total_reward = 0
        self.mu_prime = 0
        self.eid = Edge.eid
        self.possible_actions_index = possible_action_index
        self.frame_no = -1
        Edge.eid += 1

    def __repr__(self):
        return "ID " + str(self.eid) + " " + str(round(self.get_mean_reward,2)) + " PAI " + str(self.possible_actions_index) + " Act " + str(self.action)

    def __str__(self):
        return "ID " + str(self.eid) + " " + str(round(self.get_mean_reward,2)) + " PAI " + str(self.possible_actions_index) + " Act " + str(self.action)

    def get_siblings_plus_self(self):
        return self.origin.out_edges

    def get_children_edges(self):
        return self.destination.out_edges

    def get_mean_reward(self):
        return self.total_reward / self.num_visits if self.num_visits != 0 else math.inf

    #from Saffidine, 2010, UCD
    def get_mu(self, depth):
        print(self)
        if depth == 0:
            return self.get_mean_reward()
        else:
            return ((self.mu_prime * self.n_prime) + sum([f.get_mu(depth-1) * f.num_visits for f in self.get_children_edges()])) / \
                   (self.n_prime + sum([g.num_visits for g in self.get_children_edges()]))

    def get_n(self, depth):
        if depth == 0:
            return self.num_visits
        else:
            return self.n_prime + sum([f.get_n(depth-1) for f in self.get_children_edges()])

    def get_p(self, depth):
        return sum([f.get_n(depth) for f in self.get_siblings_plus_self()])
