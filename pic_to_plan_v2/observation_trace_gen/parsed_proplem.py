#import ..translate.pddl_parser
from ..translate import pddl_parser
from ..translate.pddl.conditions import Atom
from ..translate.pddl.conditions import ExistentialCondition
import pic_to_plan_v2.observation_trace_gen.parse_ontology as parse_ontology

class ParsedPDDLProblem:
    def __init__(self, domain_path, instance_path, ontology_path):
        self.domain_path = domain_path
        self.instance_path = instance_path
        self.parsed_problem_FD = pddl_parser.open(self.domain_path, self.instance_path)
        self.superclass_dict, self.individual_type_dict, self.onto = parse_ontology.parse_ontology(ontology_path)

        self.action_parameter_types_dict = {}
        # parsed_problem.objects <==> label_legend_dict.values()
        #TODO
        #all the predicates that indicate a type of object must be defined in a simple conjunctive way in the precondition of an action in the template-domain.
        #e.g., (and (graspable ?o))
        #in formulations like (and (knife ?k) (exists (?h) (and (manipulator ?h) (in_hand ?k ?h)))), then manipulator will not be added (and here it is indeed not nec as well)
        class_names = list(self.onto.classes())
        class_names = [x._name for x in class_names]

        #get all parameter names per action
        for action in self.parsed_problem_FD.actions:
            self.action_parameter_types_dict[action.name] = {}
            for param in action.parameters:
                param_name = param.name.strip("?")
                self.action_parameter_types_dict[action.name][param_name] = []

        #go through all preconditions and add them to the right parameter for each action
        for action in self.parsed_problem_FD.actions:
            for precondition in action.precondition.parts:
                if isinstance(precondition, Atom):
                    arg_name = precondition.args[0].strip("?")
                    if arg_name in self.action_parameter_types_dict[action.name].keys():
                        found_precondition_name = precondition.key[0]
                        if found_precondition_name in class_names:
                            self.action_parameter_types_dict[action.name][arg_name].append(found_precondition_name)
                            #print("\t" + found_precondition_name)
                        else:
                            #print("\tNOT A CLASS", found_precondition_name)
                            pass
                elif isinstance(precondition, ExistentialCondition):
                    print("Found existential condition. Ignore for now")

        #this is needed for signature matching in watch_video_gsrl.py
        self.action_name_list = []
        self.action_param_type_list = []
        for action_name, action_param_type_dict in self.action_parameter_types_dict.items():
            self.action_name_list.append(action_name)
            names = list(action_param_type_dict.items())
            new_names = []
            for (x, y) in names:
                new_names.append((x, [self.onto[z] for z in y]))
            self.action_param_type_list.append(new_names)