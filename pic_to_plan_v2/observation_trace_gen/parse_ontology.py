import csv
import owlready2
import dill

def parse_ontology(path):
    onto = owlready2.get_ontology(path).load()
    classes = list(onto.classes())
    individuals = list(onto.individuals())

    super_class_dict = dict()
    for c in classes:
        super_class_dict[c._name] = [c.is_a._obj]
        c_iter = c
        while(len(c_iter.is_a[0].is_a)>0):
            c_iter = c_iter.is_a[0]
            super_class_dict[c._name].append(c_iter)

    individual_type_dict = dict()
    for i in individuals:
        individual_type_dict[i._name] = i.is_a

    return super_class_dict, individual_type_dict, onto

def main_parse_ontology(ontology_path, domain_path, instance_path):
    # open ontology
    # class dict --> all superclasses of a class
    # individual_dict --> class of that individual
    class_dict, individual_dict, onto = parse_ontology(ontology_path)
    print(class_dict)
    print(individual_dict)
    print(list(class_dict.keys()))

    # write class membership predicates into domain template
    template_domain = open(domain_path, "r")
    template_domain_string = "".join(template_domain.readlines())
    class_instance_predicate_string = []
    for c in list(class_dict.keys()):
        class_instance_predicate_string.append("(" + c + " ?o)")
    class_instance_predicate_string = "\n    ".join(class_instance_predicate_string)
    parsed_template_instance_string = template_domain_string.replace("<insert-class-instance-predicates>",
                                                                     class_instance_predicate_string)

    domain_path_split = domain_path.split("/")
    domain_folder_path = "/".join(domain_path_split[:-1]) + "/"
    domain_name = domain_path_split[-1]
    domain_name_inserted_predicates = domain_name.replace(".pddl", "") + "-inserted-predicates.pddl"
    f = open(domain_folder_path + domain_name_inserted_predicates, "w")
    f.write(parsed_template_instance_string)
    f.close()

    # write objects into instance template for session start
    template_instance = open(instance_path, "r")
    template_instance_string = "".join(template_instance.readlines())
    template_instance_string = template_instance_string.replace("<insert_objects>",
                                                                "\n    ".join(list(individual_dict.keys())))

    new_predicates = []
    for o in list(individual_dict.keys()):
        for cls in class_dict[individual_dict[o][0]._name]:
            new_predicates.append("(" + cls._name + " " + o + ")")
    template_instance_string = template_instance_string.replace("<insert_class_memberships>",
                                                                "\n    ".join(new_predicates))

    instance_path_split = instance_path.split("/")
    instance_folder_path = "/".join(instance_path_split[:-1]) + "/"
    instance_name = instance_path_split[-1]
    instance_name_inserted_predicates = instance_name.replace(".pddl", "") + "-parsed-objects.pddl"
    f = open(instance_folder_path + instance_name_inserted_predicates, "w")
    f.write(template_instance_string)
    f.close()

    # write objects into instance template for "insert current state" template instance
    template_instance = open(
        instance_folder_path + instance_path_split[-1].replace(".pddl", "-insert-init.pddl"), "r")
    template_instance_string = "".join(template_instance.readlines())
    template_instance_string = template_instance_string.replace("<insert_objects>",
                                                                "\n    ".join(list(individual_dict.keys())))
    template_instance_string = template_instance_string.replace("<insert_class_memberships>",
                                                                "\n    ".join(new_predicates))

    f = open(
        instance_folder_path + instance_path_split[-1].replace(".pddl", "-parsed-objects-insert-init.pddl"),
        "w")
    f.write(template_instance_string)
    f.close()


if __name__ == "__main__":
    ontology_path = '/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/ontologies/kitchen_ontology_v1.owl'
    domain_path = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain.pddl"
    instance_path = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance.pddl"
    main_parse_ontology(ontology_path, domain_path, instance_path)