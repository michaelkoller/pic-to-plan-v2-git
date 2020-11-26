import json
from pathlib import Path
import os


replace_tuples = [("paprika_1", "paprika_powder_1"),
                  ("parika_1", "paprika_1"),
                  ("baking_paper", "baking_paper_1"),
                  ("spice_holder", "spice_holder_1"),
                  ("mais", "mais_1"),
                  ("kitchen_table", "kitchen_table_1"),
                  ("human", "human_1"),
                  ("faucet", "faucet_1"),
                  ("drawer", "drawer_1")]

for d in os.listdir(Path("/home/michael/datasets/V4RVRKitchenV1")):
    if "Sample" in d:
        paths = [Path("/home/michael/datasets/V4RVRKitchenV1", d, "RecordingsFiles/Annotations/Colormap"),
                 Path("/home/michael/datasets/V4RVRKitchenV1", d, "RecordingsFiles/Annotations/BoundingBox"),
                 Path("/home/michael/datasets/V4RVRKitchenV1", d, "RecordingsFiles/Annotations/PoseAndOrientation"),
                 Path("/home/michael/datasets/V4RVRKitchenV1", d, "RecordingsFiles/Annotations/Predicates")]
        print(paths)
        for path in paths:
            files = os.listdir(path)
            for file in files:
                print(path / Path(file))
                f = open(path / Path(file), "r")
                line = f.read()
                f.close
                for t in replace_tuples:
                    line = line.replace(t[0], t[1])
                f = open(path / Path(file), "w")
                f.write(line)
                f.close()

#--------
#naming exceptions:
#baking_paper, spice_holder, mais, kitchen_table, human, faucet, drawer

#naming errors:
#parika_1 --> paprika_1
#paprika_1 --> paprika_powder_1 (thats the spice)