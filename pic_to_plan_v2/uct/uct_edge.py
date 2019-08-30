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
        self.total_reward = 0
        self.eid = Edge.eid
        self.possible_actions_index = possible_action_index
        self.frame_no = -1
        Edge.eid += 1

    def __repr__(self):
        return "ID " + str(self.eid) + " PAI " + str(self.possible_actions_index) + " Act " + str(self.action)

    def __str__(self):
        return "ID " + str(self.eid) + " PAI " + str(self.possible_actions_index) + " Act " + str(self.action)

    def get_siblings_plus_self(self):
        return self.origin.out_edges

    def get_children_edges(self):
        return self.destination.out_edges

    def get_mean_reward(self):
        return self.total_reward / self.num_visits if self.num_visits != 0 else math.inf
