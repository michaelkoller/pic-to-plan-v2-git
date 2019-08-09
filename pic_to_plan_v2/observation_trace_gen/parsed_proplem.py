#import ..translate.pddl_parser
from ..translate import pddl_parser

class ParsedPDDLProblem:
    def __init__(self, domain_path, instance_path):
        self.domain_path = domain_path
        self.instance_path = instance_path
        self.parsed_problem_FD = pddl_parser.open(self.domain_path, self.instance_path)
        self.supertype_dict = {}
        for x in self.parsed_problem_FD.types:
            self.supertype_dict[x.name] = x.supertype_names
        self.action_parameter_types_dict = {}
        for x in self.parsed_problem_FD.actions:
            self.action_parameter_types_dict[x.name] = [y.type_name for y in x.parameters]
        self.object_type_dict = {}
        for x in self.parsed_problem_FD.objects:
            self.object_type_dict[x.name] = x.type_name
        # parsed_problem.objects <==> label_legend_dict.values()
        self.parsed_problem_objects_dict = {}
        for x in self.parsed_problem_FD.objects:
            self.parsed_problem_objects_dict[x.name] = x
