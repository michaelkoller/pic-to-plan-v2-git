# get the initial state according to the domain predicates according to the
# recorded predicates in frame 1 of the v4r vr kitchen dataset

#for now, just the stored predicates are generated using the "in" predicate

from pathlib import Path
import json
import re
from owlready2 import *

path = Path("/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/data/ontologies/TEST.owl")
onto = owlready2.get_ontology(str(path)).load()

in_predicates_path = Path("/home/michael/datasets/V4RVRKitchenV1/Sample2020-11-07-17_50_50/RecordingsFiles/Annotations/Predicates/in.json")
on_predicates_path = Path("/home/michael/datasets/V4RVRKitchenV1/Sample2020-11-07-17_50_50/RecordingsFiles/Annotations/Predicates/on.json")

###The "IN" predicate in the v4r vr kitchen dataset is used to generate the "stored" and "stored_in" predicates in the
#PDDL formulations. For ADL expressivity reasons there is the unary and binary store predicate.
unary_store = "(stored {})"
binary_store = "(stored_in {} {})"
stored_predicates = set()

location_individuals = list(onto.search(type=onto.location))
on_tuples = set() # [0] on [1]
with open(on_predicates_path) as json_file:
    data = json.load(json_file)
    for i in range(len(data["onPredicateRecords"])):
        if data["onPredicateRecords"][i]["frame"] == 1 \
                and data["onPredicateRecords"][i]["relation_type"] == "start_touching":
            on_tuples.add((data["onPredicateRecords"][i]["top_object"], data["onPredicateRecords"][i]["bottom_object"]))

#print(on_tuples)
#print(location_individuals)
with open(in_predicates_path) as json_file:
    data = json.load(json_file)
    for i in range(len(data["inPredicateRecords"])):
        entry = data["inPredicateRecords"][i]
        if entry["frame"] == 1 and entry["relation_type"] ==  "entered":
            #rules using the ontology
            inside_object_string = entry["inside_object"]
            inside_object_onto_entry = list(onto.search(iri="*#"+inside_object_string)) #a little unnecessary, could immediately use string
            if len(inside_object_onto_entry) > 0:
                if(not(inside_object_onto_entry[0] in location_individuals) #no location can be a stored thing
                    and not((entry["container_object"], entry["inside_object"]) in on_tuples)): # no container_object can be on the stored thing
                    ####print(entry["inside_object"], "in", entry["container_object"])
                    stored_predicates.add(unary_store.format(entry["inside_object"]))
                    stored_predicates.add(binary_store.format(entry["inside_object"], entry["container_object"]))
                    #print(inside_object_onto_entry[0].name)
                #inst = inside_object_onto_entry[0].is_instance_of[0]
                #print(inside_object_onto_entry[0].is_instance_of[0])
                #print(inside_object_onto_entry[0].is_instance_of == onto.location)

            #print(entry)
            #print(unary_store.format(entry["inside_object"]))
            #print(binary_store.format(entry["inside_object"], entry["container_object"]))

for x in stored_predicates:
    print(x)
###paste this output into instance-parsed-objects.pddl

###checking for some erroneous names
search_word = "Drawer_Big"
wrong_names_set = set()
for x in stored_predicates:
    if search_word in x:
        wrong_names_set.add(search_word + x.split("Drawer_Big")[-1].strip(")"))
for x in wrong_names_set:
    print(x)



#loc_0 = location_individuals[0]
#print(onto.search(type=onto.location))
#print(loc_0.name)
#print(loc_0.iri)
#print("found:", onto.search(iri="*#bin_1"))

#onto_location = onto.location
#print(onto.location)

###rules to incorporate:
#no location can be the stored object
#if objects are on top of each other, only the top object can be the stored object
#(stored X) can only appear once

#location_re = re.compile('\(location *')
#for fluent in stored_predicates:
#    if re.match(location_re, fluent):
#        print(fluent)
#matches = [s for s in  if re.match(location_re, s)]

#print(matches)

#stored_predicates_string = "\n\t".join(stored_predicates)
#print(stored_predicates_string)
#print(stored_predicates)

#put this output into the instance-v4r-vr-kitchen file
#but leave things like (hand_empty l_hand)

#stored predicates should not be symmetric, delete all stored/stored_in top_cabinet/bottom_cabinet

#if a bowl is stored in a cabinet and in another bowl, then (stored bowl_X) will appear twice --> error