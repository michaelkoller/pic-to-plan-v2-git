import math
import random
import os
import re
import copy

class Node:
    nid = 0
    re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)") #TODO pass it down from uct_search instead of setting it here

    def __init__(self, state, parent, possible_actions, prev_action, depth):
        self.state = state
        self.is_terminal = False #you always need to check with Plan Rec to get reward
        self.parent = parent
        self.num_visits = 0
        self.total_reward = 0
        self.depth = depth
        self.children = {}
        self.possible_actions = possible_actions
        self.untried_children = None #self.get_children_from_possible_actions() #call to VAL
        self.prev_action = prev_action
        self.nid = Node.nid
        Node.nid += 1

    def __repr__(self):
        return "ID " + str(self.nid) + " Depth " + str(self.depth) + " Prev Act " + str(self.prev_action)

    def __str__(self):
        return "ID " + str(self.nid) + " Depth " + str(self.depth) + " Prev Act " + str(self.prev_action)

    def is_fully_expanded(self):
        return self.untried_children is not None and len(self.untried_children) == 0

    def choose_untried_action(self):
        len_untried_children = len(self.untried_children)
        chosen_child = self.untried_children.pop(random.randint(0, len_untried_children - 1))
        self.children[chosen_child.nid] = chosen_child
        return chosen_child

    def get_children_from_possible_actions(self):
        actions_to_VAL = self.possible_actions[self.depth][1]
        pos_act_children =  self.call_VAL(actions_to_VAL)
        nop_child = Node(self.state, self, self.possible_actions, "nop", self.depth + 1)
        asdf = pos_act_children + [nop_child]
        return asdf

    def call_VAL(self, actions_to_VAL):
        current_plan_path_string = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plans/current_sas_plan_try_"
        try_action_strings = []
        for i, try_action in enumerate(actions_to_VAL):
            try_action_string = "(" + " ".join(try_action) + ")"    #create the plan for the action to try
            try_action_strings.append(try_action_string)
            f = open(current_plan_path_string+str(i), "w")
            f.write(try_action_string + "\n;cost = 1 (unit cost)")
            f.close()
        current_state_string = " ".join(self.state)
        template_instance = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects-insert-init.pddl", \
                "r")
        template_instance_string = "".join(template_instance.readlines())
        parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
        f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl", "w")
        f.write(parsed_template_instance_string)
        f.close()

        cmd = '/home/mk/Planning/VAL/validate -v /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl \
                /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/current-state-instance.pddl ' \
                + " ".join([current_plan_path_string+str(i) for i in range(len(actions_to_VAL))]) + \
                ' > /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt'
        #cmd = '/home/mk/Planning/VAL/validate -v  /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/current-state-take-put-instance-no-handempty.pddl /home/mk/PycharmProjects/pic-to-plan/val_exp/open_sas_plan > plan_val_output.txt' #check for unsatisfied precondition --> action not applicable in current state
        os.system(cmd)

        plan_val_output = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt", "r")
        plan_val_output_joined = "".join(plan_val_output.readlines())
        new_state_sets = []
        plan_val_output = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/val_output/plan_val_output.txt", "r") #TODO superfluous open, but readlines changes the iterator...
        for line in plan_val_output:
            if "Checking plan" in line:
                new_atom_added = False
                new_state_sets.append(copy.deepcopy(self.state))
            elif "Deleting" in line:
                new_atom_added = True
                m = Node.re_compiled.search(line)
                atom_to_delete = m.group(0)
                if atom_to_delete in new_state_sets[-1]:
                    new_state_sets[-1].remove(atom_to_delete)
            elif "Adding" in line:
                new_atom_added = True
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
            if new_atom_added: # and sorted_new_state_string not in state_string_to_node_id_dict.keys(): #new atom short circuits logical expression
                new_node = Node(new_state, self, self.possible_actions, try_action_strings[i], self.depth + 1)
                children.append(new_node)
        return children

    def get_best_child(self, exploration_value=0.7071067811865475): #1 / math.sqrt(2)
        best_value = -math.inf
        best_nodes = []
        for child in self.children.values():
            if child.num_visits == 0:
                node_value = math.inf
            else:
                node_value = child.total_reward / child.num_visits + \
                         exploration_value * math.sqrt(2 * math.log(self.num_visits) / child.num_visits)
            if node_value > best_value:
                best_value = node_value
                best_nodes = [child]
            elif node_value == best_value:
                best_nodes.append(child)
        return random.choice(best_nodes)

    #def default_policy(self):
    #    rewards = []
    #    return rewards #len(rewards) == |Goals|, best value per goal

    def get_untried_children_status(self):
        if self.untried_children is None:
            return "No untried children yet"
        else:
            return str(len(self.untried_children))

    def print_subtree(self):
        print("\t"*self.depth + "ID " + str(self.nid) + " Depth " + str(self.depth) + " Prev Act " + str(self.prev_action) + \
              " len_chil " + str(len(self.children) if self.children is not None else ""))
        for c in self.children.values():
            c.print_subtree()
