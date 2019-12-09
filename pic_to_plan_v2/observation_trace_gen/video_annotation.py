from os import walk
from .action_hypothesis_graph_class import ActionGraph

class VideoAnnotation:
    def __init__(self, video_dir_path, annot_dir_path, bb_to_pddl_obj_dict):
        # get video file names
        self.video_dir_path = video_dir_path
        self.video_file_paths = []
        for f in list(walk(video_dir_path))[0][2]:
            if ".avi" in f:
                self.video_file_paths.append(f)

        # get annotation file and label legend file names
        self.annot_dir_path = annot_dir_path
        self.annot_file_paths = []
        self.label_legend_paths = []
        for f in list(walk(self.annot_dir_path))[0][2]:
            if "output" in f:
                self.annot_file_paths.append(f)
            elif "label" in f:
                self.label_legend_paths.append(f)

        self.session_names = [x.split(".")[0] for x in self.video_file_paths]
        self.labels = list(bb_to_pddl_obj_dict.keys())
            #['bowl', 'bread', 'counter', 'cucumber', 'cupboard', 'cuttingboard', 'drawer', 'end', 'faucet', \
             #          'fridge', 'g_drawer', 'knife', 'l_hand', 'peel', 'peeler', 'plastic_bag', 'plastic_paper_bag', \
             #          'plate', 'r_hand', 'sink', 'spice', 'spice_holder', 'spice_shaker', 'sponge', 'towel']

    def create_single_session_dicts(self, current_session_name):
        self.current_session_name = current_session_name

        # create dict from id_no to semantic label (id_no --> label_name as in annotation file for that session)
        self.label_legend_dict = {}
        with open(self.annot_dir_path + "track_label_" + self.current_session_name + ".txt", "r") as f:
            for line in f:
                line = line.split()
                self.label_legend_dict[int(line[0])] = line[1]
        # read in annotation
        self.frame_dict = {} #this dict holds all the labels found in a certain frame
        with open(self.annot_dir_path + '/output-' + self.current_session_name + '.txt', 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.split()
                line = list(map(int, line))
                frame_no = line[5]
                if not frame_no in self.frame_dict.keys():
                    self.frame_dict[line[5]] = []
                self.frame_dict[line[5]].append(line)

        self.G = ActionGraph()
