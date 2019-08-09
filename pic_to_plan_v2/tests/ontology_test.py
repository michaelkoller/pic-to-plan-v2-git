import owlready2

#finding out how to do different queries in the ontology
path = 'file:///home/mk/Protege-5.5.0/my_ontologies/kitchen_ontology_v1.owl'
onto = owlready2.get_ontology(path).load()
print([x._name for x in list(onto.individuals())]) #show all individual names
print([x._name for x in list(onto.classes())]) #show all individual names
i0 = list(onto.individuals())[0]
print(i0.is_a)
print(i0.is_a[0].ancestors()) #get all parent classes of an individual
print(list(i0.is_a[0].subclasses())) #get all sub_classes of an individual

print("get all instances of a class")
c0 = list(onto.classes())[1]
print(list(onto.classes()))
print(c0.instances()) #get all parent classes of an individual

#TODO
#and now use this to get the type of an individual for finding out if it's a hand for touches_w_hand
#use it to find out if it has the right type signature for an action
#add a class "manipulator" to the ontology, make hand a subclass
#then query the all manipulator instances, instead of hard-coding "hand"
