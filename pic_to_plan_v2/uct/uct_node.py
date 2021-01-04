import random
import re
from pic_to_plan_v2.settings import ROOT_DIR
from pathlib import Path
import os
import copy
from pic_to_plan_v2.uct.uct_edge import Edge


class Node:
    nid = 0
    re_compiled = re.compile(r"\([A-Za-z0-9_ ]+\)")

    def __init__(self, state, in_edge, possible_actions_session, domain_inserted_predicates_path,
                 instance_parsed_objects_path):
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
            chosen_child_node, chosen_child_edge = \
                self.untried_children.pop(random.randint(0, len(self.untried_children) - 1))
            self.out_edges.append(chosen_child_edge)
            return chosen_child_node, chosen_child_edge

    def get_children_from_possible_actions(self):
        pos_act_children = self.call_VAL()
        return pos_act_children

    def call_VAL(self):  # not using n_iter. it's just a call to get_min_in_edge
        current_plan_path_string = Path(ROOT_DIR) / Path("pddl/plans/current_sas_plan_try_")

        try_action_strings = []
        plan_file_names = []
        pos_act_indices = []
        for pos_act_index in range(self.get_lowest_possible_action_index(), len(self.possible_actions)):
            for i, try_action in enumerate(self.possible_actions[pos_act_index][1]):
                try_action_string = "(" + " ".join(try_action) + ")"  # create the plan for the action to try
                if try_action_string not in try_action_strings:
                    try_action_strings.append(try_action_string)
                    plan_file_names.append(str(current_plan_path_string)+str(pos_act_index)+"_"+str(i))
                    pos_act_indices.append(pos_act_index)
                    f = open(plan_file_names[-1], "w")
                    f.write(try_action_string + "\n;cost = 1 (unit cost)")
                    f.close()
        current_state_string = " ".join(self.state)
        template_instance = open(self.instance_parsed_objects_path.replace(".pddl", "-insert-init.pddl"), "r")
        template_instance_string = "".join(template_instance.readlines())
        parsed_template_instance_string = template_instance_string.replace("<insert_init>", current_state_string)
        f = open(str(Path(ROOT_DIR) / Path("pddl/instances/current-state-instance.pddl")), "w")
        f.write(parsed_template_instance_string)
        f.close()
        cmd = str(Path(ROOT_DIR,  "VAL/validate")) + " -v " + self.domain_inserted_predicates_path + " " + \
            str(Path(ROOT_DIR, "pddl/instances/current-state-instance.pddl")) + " " + \
            " ".join(plan_file_names) + \
            " > " + str(Path(ROOT_DIR, "pddl/val_output/plan_val_output.txt"))
        os.system(cmd)
        new_state_sets = []
        # TODO superfluous open, but readlines changes the iterator...
        plan_val_output = Path(ROOT_DIR, "pddl/val_output/plan_val_output.txt").open(mode="r")
        new_atom_added_list = []
        for line in plan_val_output:
            if "Checking plan" in line:
                new_atom_added_list.append(False)
                new_state_sets.append(copy.deepcopy(self.state))
            elif "Deleting" in line:
                new_atom_added_list[-1] = True
                # actually not really the correct regex, because (asdf asdf) (asdf asdf)
                # will be recognized as 1 occurrence, but here only ever 1 atom per line appears
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
            # and sorted_new_state_string not in state_string_to_node_id_dict.keys():
            # new atom short circuits logical expression
            if new_atom_added_list[i]:
                # origin, destination, action, possible_action_index):
                new_edge = Edge(self, None, try_action_strings[i], pos_act_indices[i])
                new_node = Node(new_state, new_edge, self.possible_actions, self.domain_inserted_predicates_path,
                                self.instance_parsed_objects_path)  # state, in_edge, possible_actions):
                new_edge.destination = new_node
                children.append((new_node, new_edge))
        return children

    def get_lowest_possible_action_index(self):
        return min([e.possible_action_index for e in self.in_edges])
