import json
from pathlib import Path
import owlready2

# object_pos_rot_path = Path(r"C:\Users\kolle\Documents\RecordingsForRender\Sample2020-11-12-15_21_20\RecordingsFiles\Annotations\PoseAndOrientation\position_and_orientation_1.json")
# with open(object_pos_rot_path) as json_file:
#     data = json.load(json_file)
#     for obj in data["positionAndRotationFrameArr"][0]["objectPositionAndRotationArr"]:
#         print(obj["name"])

colormap_path = Path(r"C:\Users\kolle\Documents\RecordingsForRender\Sample2020-11-12-15_21_20\RecordingsFiles\Annotations\Colormap\colormap.json")
tracked_objects = []
with open(colormap_path) as json_file:
    data = json.load(json_file)
    for obj in data["object_colors"]:
        tracked_objects.append(obj["name"])

tracked_objects = sorted(tracked_objects)
#for entry in tracked_objects:
#    print(entry)

    #at cup_1

onto = owlready2.get_ontology(r"C:\Users\kolle\Documents\GitHub\pic-to-plan-v2-git\pic_to_plan_v2\data\ontologies\v4r_kitchen_ontology_v2.owl").load()
individuals = list(onto.individuals())
individuals = [str(i).split(".")[1] for i in individuals]
#for individual in individuals:
#    print(individual)

bad_names = ["baking_paper", "spice_holder", "mais", "kitchen_table", "human", "faucet", "drawer"]

print("INDIVIDUALS NOT IN TRACKED OBJECTS")
for individual in individuals:
    if individual not in tracked_objects:
        print(individual)

print("TRACKED OBJECTS NOT IN INDIVIDUALS")
print("These are bad naming conventions. Should be changed in unity project")
for tracked_object in tracked_objects:
    if tracked_object not in individuals:
        print(tracked_object)

#naming exceptions:
#baking_paper, spice_holder, mais, kitchen_table, human, faucet, drawer

#naming errors:
#parika_1