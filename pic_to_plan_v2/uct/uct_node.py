import math
import random
import os
import re
import copy
import time
import pic_to_plan_v2.uct.uct_edge as uct_edge_mod

class Node:
    nid = 0
    re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)") #TODO pass it down from uct_search instead of setting it here

    def __init__(self, state, in_edge, possible_actions, domain_path_inserted_predicates, instance_parsed_objects_path):
        self.state = state
        self.state_string = " ".join(sorted(list(self.state)))
        self.hash_value = self.state_string.__hash__()
        self.is_terminal = False #you always need to check with Plan Rec to get reward
        self.in_edges = [in_edge]
        self.out_edges = []
        self.possible_actions = possible_actions
        self.untried_children = None #self.get_children_from_possible_actions() #call to VAL
        self.nid = Node.nid
        self.expanded_possible_action_indices = []
        self.instance_parsed_objects_path = instance_parsed_objects_path
        self.domain_path_inserted_predicates = domain_path_inserted_predicates
        Node.nid += 1

    def __repr__(self):
        return "ID " + str(self.nid) + " " + self.state_string

    def __str__(self):
        return "ID " + str(self.nid) + " " + self.state_string

    def __hash__(self):
        return self.hash_value

    def is_fully_expanded(self):
        return self.untried_children is not None and len(self.untried_children) == 0

    def choose_untried_action(self):
        len_untried_children = len(self.untried_children)
        chosen_child_edge_plus_node = self.untried_children.pop(random.randint(0, len_untried_children - 1))
        self.out_edges.append(chosen_child_edge_plus_node[0])
        return chosen_child_edge_plus_node

    def get_children_from_possible_actions(self):
        pos_act_children = self.call_VAL(self.possible_actions[self.get_min_in_edge_possible_action_index()][1])
        return pos_act_children

    def get_min_in_edge_possible_action_index(self):
        return min([e.possible_actions_index for e in self.in_edges]) if self.in_edges != [None] else 0

    def call_VAL(self, n_iter):
        #TODO create unique place for current sas plans
        current_plan_path_string = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plans/current_sas_plan_try_"

        try_action_strings = []
        plan_file_names = []
        pos_act_indices = []
        for pos_act_index in range(self.get_min_in_edge_possible_action_index(), len(self.possible_actions)):
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
        #"/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects-insert-init.pddl"
        template_instance = open(self.instance_parsed_objects_path.replace(".pddl", "-insert-init.pddl"), "r")
        template_instance_string = "".join(template_instance.readlines())
        parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
        #TODO make unique current state instances
        f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl", "w")
        f.write(parsed_template_instance_string)
        f.close()
        cmd = '/home/mk/Planning/VAL/validate -v ' + self.domain_path_inserted_predicates + \
                        ' /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl ' \
              + " ".join(plan_file_names) + \
              ' > /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt'
        ###hardcoded files
        # cmd = '/home/mk/Planning/VAL/validate -v /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl \
        #         /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl ' \
        #         + " ".join(plan_file_names) + \
        #         ' > /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt'
        ###end hardcoded
        #cmd = '/home/mk/Planning/VAL/validate -v  /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/current-state-take-put-instance-no-handempty.pddl /home/mk/PycharmProjects/pic-to-plan/val_exp/open_sas_plan > plan_val_output.txt' #check for unsatisfied precondition --> action not applicable in current state
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
                m = Node.re_compiled.search(line)
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
            #without state_string_to_node_id_dict I will have duplicate states in the tree. lets see if uct can handle it
            #TODO introduce a dict to look up existing states. if existing states occur, allow multiple parents.
            #this results in a DAG, and needs to update the backup fct. take care of duplicate rewards as paths remerge later,
            #depth will be more complex to define, nop action maybe useless afterwards
            if new_atom_added_list[i]: # and sorted_new_state_string not in state_string_to_node_id_dict.keys(): #new atom short circuits logical expression
                new_edge = uct_edge_mod.Edge(self, None, try_action_strings[i], pos_act_indices[i]) #origin, destination, action, possible_action_index):
                new_node = Node(new_state, new_edge, self.possible_actions, self.domain_path_inserted_predicates, self.instance_parsed_objects_path) #state, in_edge, possible_actions):
                new_edge.destination = new_node
                children.append((new_edge, new_node))
        return children

    def get_best_child(self, exploration_value=1.4142135623730951, d_1=1, d_2=1, d_3=1): #math.sqrt(2)
        best_value = -math.inf
        best_edges = []
        for e in self.out_edges:
            if e.num_visits == 0:
                edge_value = math.inf
            else:
                #Standart UCT
                # edge_value = e.total_reward / e.num_visits + \
                #              exploration_value * math.sqrt(math.log(self.get_visit_count()) / e.num_visits)
                #Saffidine, 2010, UCD
                edge_value = e.get_mu(d_1) + \
                             exploration_value * math.sqrt(math.log(e.get_p(d_2)) / e.get_n(d_3))
            if edge_value > best_value:
                best_value = edge_value
                best_edges = [e]
            elif edge_value == best_value:
                best_edges.append(e)
        chosen_edge = random.choice(best_edges)
        return chosen_edge, chosen_edge.destination

    def get_visit_count(self):
        self.num_visits = sum([e.num_visits for e in self.in_edges]) if None not in self.in_edges else 1
        return self.num_visits

    def get_total_reward(self):
        self.total_reward = sum([e.total_reward for e in self.in_edges]) if self.in_edges != [None] else 0
        return self.total_reward

    def get_mean_reward(self):
        self.mean_reward = self.get_total_reward() / self.get_visit_count()  if self.get_visit_count() != 0 else math.inf
        return self.mean_reward

if __name__ == "__main__":
    a = dict()
    n1 = Node(["a", "b"], None, None, None, None)
    n2 = Node(["a", "b"], None, None, None, None)
    n3 = Node(["a", "c"], None, None, None, None)
    print(n1.state_string)
    print(n1.__hash__())
    print(n2.state_string)
    print(n2.__hash__())
    print(n3.state_string)
    print(n3.__hash__())
    a[n1.__hash__()] = n1
    print(a)
    print(n1.__hash__() in a)
    print(n2.__hash__() in a)
    print(n3.__hash__() in a)
    n1.a = 0
    n2.a = 1
    if n2.__hash__() not in a:
        a[n2.__hash__()] = n2
    print(a[n2.__hash__()].a)