import csv
import owlready2
import dill

def parse_ontology():
    path = 'file:///home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/ontologies/kitchen_ontology_v1.owl'
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

if __name__ == "__main__":
    #open ontology
    #class dict --> all superclasses of a class
    #individual_dict --> class of that individual
    class_dict, individual_dict, onto = parse_ontology()
    print(class_dict)
    print(individual_dict)
    print(list(class_dict.keys()))

    #write class membership predicates into domain template
    template_domain = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain.pddl", "r")
    template_domain_string = "".join(template_domain.readlines())
    class_instance_predicate_string = ";the following defines class membership predicates\n"
    for c in list(class_dict.keys()):
        class_instance_predicate_string += "("+ c + " ?o)\n\t"
    class_instance_predicate_string += ";end class membership predicates"
    parsed_template_instance_string = template_domain_string.replace("<insert-class-instance-predicates>", class_instance_predicate_string)
    f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl", "w")
    f.write(parsed_template_instance_string)
    f.close()

    #write objects into instance template
    template_instance = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance.pddl", "r")
    template_instance_string = "".join(template_instance.readlines())
    template_instance_string = template_instance_string.replace("<insert_objects>", "\n\t".join(list(individual_dict.keys())))

    new_predicates = []
    for o in list(individual_dict.keys()):
        for cls in class_dict[individual_dict[o][0]._name]:
            new_predicates.append("(" + cls._name + " " + o + ")")
    new_predicates.append(";end of class membership predicates")
    template_instance_string = template_instance_string.replace("<insert_class_memberships>", "\n\t".join(new_predicates))

    f = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects.pddl", "w")
    f.write(template_instance_string)
    f.close()
