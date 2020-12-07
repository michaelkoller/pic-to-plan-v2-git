import os
from .action_hypothesis_graph_class import ActionGraph
from pathlib import Path
import pic_to_plan_v2.settings as settings
import json

class VideoAnnotation:
    def __init__(self, video_dir_path, annot_dir_path, bb_to_pddl_obj_dict):
        # get video file names
        self.video_dir_path = video_dir_path
        self.video_file_paths = []
        print(video_dir_path)
        for f in list(os.walk(str(video_dir_path)))[0][2]:
            if ".avi" in f:
                self.video_file_paths.append(f)

        # get annotation file and label legend file names
        self.annot_dir_path = annot_dir_path
        self.annot_file_paths = []
        self.label_legend_paths = []
        for f in list(os.walk(self.annot_dir_path))[0][2]:
            if "output" in f:
                self.annot_file_paths.append(f)
            elif "label" in f:
                self.label_legend_paths.append(f)
        self.frame_dict = {}

        self.session_names = [x.split(".")[0] for x in self.video_file_paths]
        self.labels = list(bb_to_pddl_obj_dict.keys())
            #['bowl', 'bread', 'counter', 'cucumber', 'cupboard', 'cuttingboard', 'drawer', 'end', 'faucet', \
             #          'fridge', 'g_drawer', 'knife', 'l_hand', 'peel', 'peeler', 'plastic_bag', 'plastic_paper_bag', \
             #          'plate', 'r_hand', 'sink', 'spice', 'spice_holder', 'spice_shaker', 'sponge', 'towel']

    def create_single_session_dicts(self, current_session_name):
        self.current_session_name = current_session_name

        # create dict from id_no to semantic label (id_no --> label_name as in annotation file for that session)
        self.label_legend_dict = {}

        with open(str(self.annot_dir_path / Path("track_label_" + self.current_session_name + ".txt")), "r") as f:
            for line in f:
                line = line.split()
                self.label_legend_dict[int(line[0])] = line[1]
        # read in annotation
        self.frame_dict = {}  # this dict holds all the labels found in a certain frame
        with open(str(self.annot_dir_path / Path('output-' + self.current_session_name + '.txt')), 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.split()
                line = list(map(int, line))
                frame_no = line[5]
                if not frame_no in self.frame_dict.keys():
                    self.frame_dict[line[5]] = []
                self.frame_dict[line[5]].append(line)


class VideoAnnotationV4RVRK:
    def __init__(self, bb_to_pddl_obj_dict):
        self.video_dir_path = Path(settings.ARGS.sample, "RecordingsFiles/Videos/Cam1")
        self.video_file_paths = ["video_rgb.avi"]
        self.annot_dir_path = Path(settings.ARGS.sample, "RecordingsFiles/Annotations/BoundingBox")
        self.annot_file_paths = []
        self.label_legend_paths = []
        for f in list(os.walk(self.annot_dir_path))[0][2]:
            self.annot_file_paths.append(f)

        def bb_file_sort(file_path_string):
            return int(file_path_string.split(".")[0].split("_")[-1])
        self.annot_file_paths = sorted(self.annot_file_paths, key=bb_file_sort)
        print(self.annot_file_paths)
        self.labels = list(bb_to_pddl_obj_dict.keys())
        self.G = ActionGraph()
        self.current_session_name = settings.ARGS.sample.split(os.sep)[-1]
        self.label_legend_dict = bb_to_pddl_obj_dict
        self.frame_dict = {}
        for file_path in self.annot_file_paths:
            file = open(Path(self.annot_dir_path, file_path))
            data = json.load(file)
            file.close()
            for frame in data["bb_frame_arr"]:
                for entry in frame["bb_obect_arr"]:
                    # the last 3 values are there to describe the values used in gsrl
                    a = [entry["name"], int(entry["x_min"]), int(entry["y_min"]), int(entry["x_max"]),
                         int(entry["y_max"]), int(frame["frame_number"]), 0,0,0]
                    self.frame_dict.setdefault(int(frame["frame_number"]), []).append(a)

