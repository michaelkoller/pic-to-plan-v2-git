import cv2
import copy
import itertools
import pic_to_plan_v2.observation_trace_gen.parsed_proplem as parsed_problem_mod
import pic_to_plan_v2.observation_trace_gen.video_annotation as video_annotation_mod
import pickle
import pic_to_plan_v2.settings as settings
from pathlib import Path
import os
import re

#['s13-d25', 's28-d25', 's37-d25', 's21-d21', 's31-d25', 's23-d21', 's13-d21', 's27-d21', 's37-d21', 's22-d25']
#label names from all sessions ['bowl', 'bread', 'counter', 'cucumber', 'cupboard', 'cuttingboard', 'drawer', 'end', 'faucet', 'fridge', 'g_drawer', 'knife', 'l_hand', 'peel', 'peeler', 'plastic_bag', 'plastic_paper_bag', 'plate', 'r_hand', 'sink', 'spice', 'spice_holder', 'spice_shaker', 'sponge', 'towel']

def show_annotation(p_p, v_a, bb_to_pddl_obj_dict, touch_events, possible_actions_session):
    # read in video and draw annotation
    assert(settings.ARGS.dataset == "v4rvrkitchenv1", "Wrong dataset: " + settings.ARGS.dataset)
    vid_path =  Path(settings.ARGS.sample, "RecordingsFiles/Videos/Cam1/video-rgb.avi")
    print("VIDEO TO WATCH", vid_path)
    cap = cv2.VideoCapture(str(vid_path))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    out = cv2.VideoWriter('~/output.avi', fourcc, 30.0, size)

    current_frame = 0
    font = cv2.FONT_HERSHEY_PLAIN
    current_touching_objects = set()
    prev_touching_objects = set()
    while (cap.isOpened()):
        instantiated_actions = []
        ret, frame = cap.read()
        added_objects = []#add here the annotated objects
        if current_frame in v_a.frame_dict.keys():
            for annotated_obj in v_a.frame_dict[current_frame]:
                cv2.rectangle(frame, (2 * annotated_obj[3], 2 * annotated_obj[2]),
                              (2 * annotated_obj[1], 2 * annotated_obj[4]), (0, 255, 0), 1)
                print(frame)
                print(annotated_obj[0])
                print(v_a.label_legend_dict[annotated_obj[0]][0])
                print(annotated_obj[1])
                print(annotated_obj[2])
                ###Handle names of cut objects, which have added 0s and 1s at the end of the name
                #Need to get the original object name, since this is in the dict
                print(annotated_obj[0])
                key = re.match("*?[0-9]", annotated_obj[0])
                print("KEY", key)

                cv2.putText(frame, v_a.label_legend_dict[key][0],
                            (2 * annotated_obj[1] + 5, 2 * annotated_obj[2] + 15), font, 1, (255, 255, 255), 1,
                            cv2.LINE_4)
                #go through all previously added objects and see if the rectangles overlap
                x_min_new, y_min_new, x_max_new, y_max_new = annotated_obj[1], annotated_obj[2], annotated_obj[3], annotated_obj[4]
                for prev_added in added_objects:
                    x_min, y_min, x_max, y_max = prev_added[1], prev_added[2], prev_added[3], prev_added[4]

                    if x_min > x_max_new or x_max < x_min_new:
                        current_touching_objects.discard(tuple(sorted((prev_added[0], annotated_obj[0]))))
                    elif y_min > y_max_new or y_max < y_min_new:
                        current_touching_objects.discard(tuple(sorted((prev_added[0], annotated_obj[0]))))
                    else:
                        cv2.rectangle(frame, (2 * max(x_min,x_min_new), 2 * max(y_min,y_min_new)),
                                      (2 * min(x_max,x_max_new), 2 * min(y_max,y_max_new)), (0, 0, 255), 1)
                        current_touching_objects.add(tuple(sorted((prev_added[0], annotated_obj[0]))))
                added_objects.append(annotated_obj)

        if not(frame is None):
            cv2.imshow('frame', frame)
            out.write(frame)
            pass
        else:
            cap.release()
            out.release()
            cv2.destroyAllWindows()
        current_frame += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('p'):
            while True:
                if cv2.waitKey(1) & 0xFF == ord('p'):
                    break

        detected_added_touches = list(current_touching_objects - prev_touching_objects)
        detected_removed_touches = list(prev_touching_objects - current_touching_objects)
        detected_touches = detected_added_touches + detected_removed_touches #using "extend" results in None, but I want [] if empty

        # for x in detected_touches:
        #     l0_bb_name = v_a.label_legend_dict[x[0]]
        #     l1_bb_name = v_a.label_legend_dict[x[1]]
        #     # TODO here are the multiple instances of an object type in bb_to_pddl_obj_dict[l0_bb_name]
        #     # if multiple instances exist in a scene, you need some tracking to see which instances are assigned, etc...
        #     # ignore this for now...
        #     l0_pddl_name = bb_to_pddl_obj_dict[l0_bb_name][0]
        #     l1_pddl_name = bb_to_pddl_obj_dict[l1_bb_name][0]
        #     l0_pddl_type = p_p.individual_type_dict[l0_pddl_name][0]._name #TODO does the onto.individuals just return lists or did I add smthng?
        #     l1_pddl_type = p_p.individual_type_dict[l1_pddl_name][0]._name
        #     l0_superclasses = p_p.superclass_dict[l0_pddl_type]
        #     l1_superclasses = p_p.superclass_dict[l1_pddl_type]
        #     for i, action in enumerate(p_p.action_param_type_list):
        #         a = set(l0_superclasses).issuperset(set(action[0][1]))
        #         b = set(l1_superclasses).issuperset(set(action[1][1]))
        #         c = set(l1_superclasses).issuperset(set(action[0][1]))
        #         d = set(l0_superclasses).issuperset(set(action[1][1]))
        #         if a and b: #TODO these 2 ifs should catch cases, where two operators are of same type, like (unstack blockA blockB)
        #             #print(p_p.action_name_list[i], l0_pddl_name, l1_pddl_name, action)
        #             instantiated_actions.append((p_p.action_name_list[i], l0_pddl_name, l1_pddl_name))
        #         if c and d:
        #             #print(p_p.action_name_list[i], l1_pddl_name, l0_pddl_name, action)
        #             instantiated_actions.append((p_p.action_name_list[i], l1_pddl_name, l0_pddl_name))
        #
        # if len(instantiated_actions) > 0:
        #     print(current_frame, instantiated_actions)
        #     possible_actions_session.append((current_frame, instantiated_actions))
        # if len(detected_touches) > 0:
        #     touch_events.append((current_frame, detected_touches))
        #
        # #TODO add hysteresis
        # #TODO add object tracking / managing active instances of object classes
        #
        # prev_touching_objects = copy.deepcopy(current_touching_objects)
        # #if len(detected_touches) > 0:
        # #    print(detected_touches)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Done watching video")

def main_watch_video(domain_path, instance_path, session, ontology_path): #input grounded role labeling dataset session here
    domain_path_inserted_predicates = str(domain_path).replace(".pddl", "-inserted-predicates.pddl")
    instance_path_inserted_predicates = str(instance_path).replace(".pddl", "-parsed-objects.pddl")
    print(domain_path_inserted_predicates)
    print(instance_path_inserted_predicates)
    print(ontology_path)
    my_parsed_problem = parsed_problem_mod.ParsedPDDLProblem(domain_path_inserted_predicates, \
                                                            instance_path_inserted_predicates, ontology_path)

    #i create this dict for translating the names from the bounding boxes to the names used in pddl,
    #but for the v4r vr kitchen dataset its the same name
    bb_to_pddl_obj_dict = {}
    for key in my_parsed_problem.individual_type_dict.keys():
        bb_to_pddl_obj_dict[key] = [key]

    assert(settings.ARGS.dataset == "v4rvrkitchenv1", "WRONG watch_video_X.py script for specified dataset:", settings.ARGS.dataset)

    video_annotation = video_annotation_mod.VideoAnnotationV4RVRK(bb_to_pddl_obj_dict)
    current_session = video_annotation.current_session_name
    touch_events = []                       #all binary starts and ends of overlaps between two objects (frame_no, [all touches])
    possible_actions_session = []          #all actions from manipulator_events and non_manipulator_events where the object predicates match to an action (frame_no, [all_actions])
    print(current_session)
    show_annotation(my_parsed_problem, video_annotation, bb_to_pddl_obj_dict, touch_events, possible_actions_session)
    #show_annotation(random.choice(session_names), parsed_problem)
    print(current_session, "done")
    pickle.dump(touch_events, \
                open(str(Path(settings.ROOT_DIR) / Path("data/overlap_detections/touch_events_"+str(current_session)+".p")), "wb"))
    pickle.dump(possible_actions_session, \
                open(str(Path(settings.ROOT_DIR) / Path("data/possible_actions/possible_actions_session_"+str(current_session)+".p")), "wb"))

if __name__ == "__main__":
    main_watch_video()