import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CORES = 2
PROB_PLAN_REC_COPIES = 10
PYTHON2_PATH = "/home/michael/venv/probplanrec/bin/python2"
RESULTS_DIR = os.path.join(ROOT_DIR, "data/results")

#argparse settings available for all scripts
ARGS = None

#these should not be here but in argpars
VIDEO_DIR_PATH = "/home/michael/datasets/GroundedSemanticRoleLabeling/Video_annotation/Video_annotation/Videos"
ANNOT_DIR_PATH ="/home/michael/datasets/GroundedSemanticRoleLabeling/Video_annotation/Video_annotation"
V4R_DATASET_PATH = "/home/michael/datasets/V4RVRKitchenV1"
V4R_TEST_SAMPLE_NAME = "Sample2020-11-12-15_27_53"

def set_args(args):
    global ARGS
    ARGS = args