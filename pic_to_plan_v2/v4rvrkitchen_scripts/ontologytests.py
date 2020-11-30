from owlready2 import *
from pathlib import Path

path = Path("/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/data/ontologies/TEST.owl")
onto = owlready2.get_ontology(str(path)).load()

with onto:
    sync_reasoner_pellet()
    print(list(onto.individuals()))
    a = list(onto.individuals())[0]
    print(a.is_a)
