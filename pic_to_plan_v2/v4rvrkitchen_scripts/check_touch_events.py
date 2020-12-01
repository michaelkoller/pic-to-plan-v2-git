import pickle

file_path_touch_events = "/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/data/overlap_detections/touch_events_Sample2020-11-07-17_50_50.p"
file_path_possible_actions = "/home/michael/git/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_Sample2020-11-07-17_50_50.p"

touch_events = pickle.load( open( file_path_touch_events, "rb" ) )
possible_actions = pickle.load( open( file_path_possible_actions, "rb" ) )

print("done")