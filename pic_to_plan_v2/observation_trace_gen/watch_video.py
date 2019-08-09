####current version! aug 5
import cv2
import copy
import itertools
import pic_to_plan_v2.observation_trace_gen.parsed_proplem as parsed_problem_mod
import pic_to_plan_v2.observation_trace_gen.video_annotation as video_annotation_mod
import pickle

#['s13-d25', 's28-d25', 's37-d25', 's21-d21', 's31-d25', 's23-d21', 's13-d21', 's27-d21', 's37-d21', 's22-d25']
#label names from all sessions ['bowl', 'bread', 'counter', 'cucumber', 'cupboard', 'cuttingboard', 'drawer', 'end', 'faucet', 'fridge', 'g_drawer', 'knife', 'l_hand', 'peel', 'peeler', 'plastic_bag', 'plastic_paper_bag', 'plate', 'r_hand', 'sink', 'spice', 'spice_holder', 'spice_shaker', 'sponge', 'towel']

#exhaust_list = [sorted(list(x)) for x in list(itertools.product(*sorted_bb_objs))]

### still need to catch following case:
### if action signature has mutliple instances of one type, e.g. stack(box1, box2), you need to show all permutations
def compare_action_signatures(detected_added_touches_w_hand, bb_to_pddl_obj_dict, v_a, p_p):
    instantiated_action_names = []
    for det_touches in detected_added_touches_w_hand:
        pddl_name_0, pddl_name_1 = get_pddl_names_of_one_touching_pair(det_touches, v_a, p_p, bb_to_pddl_obj_dict) #TODO distinguish between different instantiations of a tracked label! --> use track number + label name
        det_touch_type_0 = p_p.object_type_dict[pddl_name_0]
        det_touch_supertype_0 = p_p.supertype_dict[det_touch_type_0]

        det_touch_type_1 = p_p.object_type_dict[pddl_name_1]
        det_touch_supertype_1 = p_p.supertype_dict[det_touch_type_1]

        types_0 = set(det_touch_supertype_0)
        types_0.add(det_touch_type_0)
        types_1 = set(det_touch_supertype_1)
        types_1.add(det_touch_type_1)

        exhaust_list = [sorted(list(x)) for x in list(itertools.product(types_0, types_1))] #all type combinations the detected objects could be, sorted
        for action in p_p.parsed_problem_FD.actions:
            action_signature_types = sorted([x.type_name for x in action.parameters]) #the 1 sorted type signature of the currently considered action
            if action_signature_types in exhaust_list:
                if action.parameters[0].type_name in types_0 and action.parameters[1].type_name in types_1:
                    instantiated_action_names.append((action.name, pddl_name_0, pddl_name_1))
                if action.parameters[0].type_name in types_1 and action.parameters[1].type_name in types_0:
                    instantiated_action_names.append((action.name, pddl_name_1, pddl_name_0))
    return instantiated_action_names

def get_pddl_names_of_current_touching_objects(current_touching_objects, v_a, p_p, bb_to_pddl_obj_dict):
    names = []
    for x in current_touching_objects:
        names.append(get_pddl_names_of_one_touching_pair(x, v_a, p_p, bb_to_pddl_obj_dict))
    return names

def get_pddl_names_of_one_touching_pair(pair, v_a, p_p, bb_to_pddl_obj_dict):
    l0_bb_name = v_a.label_legend_dict[pair[0]]
    l1_bb_name = v_a.label_legend_dict[pair[1]]
    l0_pddl_name = bb_to_pddl_obj_dict[l0_bb_name]
    l1_pddl_name = bb_to_pddl_obj_dict[l1_bb_name]
    return (l0_pddl_name,l1_pddl_name)

def get_pddl_super_types(x, v_a, p_p, bb_to_pddl_obj_dict):
    types = []
    l0_bb_name = v_a.label_legend_dict[x[0]]
    l1_bb_name = v_a.label_legend_dict[x[1]]
    l0_pddl_name = bb_to_pddl_obj_dict[l0_bb_name]
    l1_pddl_name = bb_to_pddl_obj_dict[l1_bb_name]
    l0_pddl_type = p_p.object_type_dict[l0_pddl_name]
    l1_pddl_type = p_p.object_type_dict[l1_pddl_name]
    return (l0_pddl_type, l1_pddl_type)

def show_annotation(p_p, v_a, bb_to_pddl_obj_dict, detected_added_touches_w_hand_session, possible_actions_session, detected_added_touches_session):
    # read in video and draw annotation
    cap = cv2.VideoCapture(
        v_a.video_dir_path + v_a.current_session_name + '.avi')
    current_frame = 0
    font = cv2.FONT_HERSHEY_PLAIN
    current_touching_objects = set()
    prev_touching_objects = set()
    while (cap.isOpened()):
        ret, frame = cap.read()
        added_objects = []#add here the annotated objects
        if current_frame in v_a.frame_dict.keys():
            for annotated_obj in v_a.frame_dict[current_frame]:
                if annotated_obj[7] != 1 and annotated_obj[6] != 1:  # only draw if obj is not occluded and not lost
                    cv2.rectangle(frame, (2 * annotated_obj[3], 2 * annotated_obj[2]),
                                  (2 * annotated_obj[1], 2 * annotated_obj[4]), (0, 255, 0), 1)
                    cv2.putText(frame, v_a.label_legend_dict[annotated_obj[0]],
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
            pass
        else:
            cap.release()
            cv2.destroyAllWindows()
        current_frame += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        detected_added_touches = list(current_touching_objects - prev_touching_objects)
        detected_added_touches_w_hand = set()
        for x in detected_added_touches:
            l0_bb_name = v_a.label_legend_dict[x[0]]
            l1_bb_name = v_a.label_legend_dict[x[1]]
            l0_pddl_name = bb_to_pddl_obj_dict[l0_bb_name]
            l1_pddl_name = bb_to_pddl_obj_dict[l1_bb_name]
            l0_pddl_type = p_p.object_type_dict[l0_pddl_name]
            l1_pddl_type = p_p.object_type_dict[l1_pddl_name]
            if ("hand" != l0_pddl_type and "hand" == l1_pddl_type) or \
                    ("hand" == l0_pddl_type and "hand" != l1_pddl_type):
                detected_added_touches_w_hand.add((min(x[0], x[1]), max(x[0], x[1]))) #add numbers sorted


        if len(detected_added_touches_w_hand) > 0:
            print("frame_no:", current_frame, get_pddl_names_of_current_touching_objects(current_touching_objects, v_a, p_p, bb_to_pddl_obj_dict))
            named_touches = [(v_a.label_legend_dict[x[0]], v_a.label_legend_dict[x[1]]) for x in detected_added_touches_w_hand]
            ###use graph here or not?
            ###v_a.G.update([(0,"\n".join(x)) for x in named_touches])
            prev_touching_objects = copy.deepcopy(current_touching_objects)
            possible_actions = compare_action_signatures(detected_added_touches_w_hand, bb_to_pddl_obj_dict, v_a, p_p)
            if len(possible_actions) > 0:
                print("poss act:")
                for x in possible_actions:
                    print(x)
                possible_actions_session.append((current_frame, possible_actions))
            detected_added_touches_w_hand_session.append((current_frame, detected_added_touches_w_hand))
            #cv2.waitKey(0)
        if len(detected_added_touches) > 0:
            detected_added_touches_session.append((current_frame, detected_added_touches))
        #find way to keep track of active objects, like tools!

    cap.release()
    cv2.destroyAllWindows()

def main():
    #my_parsed_problem = ParsedPDDLProblem("take-put-domain.pddl", "take-put-instance.pddl")

    # dict from bounding boxes to parsed_problem_objects_dict.keys()
    bb_to_pddl_obj_dict = {'plastic_bag': ['plastic_bag1'], 'plastic_paper_bag': ['plastic_paper_bag1'], 'g_drawer': ['g_drawer1'],
     'sponge': ['sponge1'], 'drawer': ['drawer1', 'drawer2'], 'cuttingboard': ['cuttingboard1'], 'end': ['end1'],
     'bowl': ['bowl1'], 'r_hand': ['r_hand'], 'bread': ['bread1', 'bread2', 'bread3'], 'knife': ['knife1'], 'plate': ['plate1'],
     'cupboard': ['cupboard1'], 'peel': ['peel1'], 'fridge': ['fridge1'], 'cucumber': ['cucumber1'], 'sink': ['sink1'],
     'peeler': ['peeler1'], 'spice': ['spice1'], 'faucet': ['faucet1'], 'spice_holder': ['spice_holder1'],
     'towel': ['towel1'], 'counter': ['counter1'], 'spice_shaker': ['spice_shaker1'], 'l_hand': ['l_hand'],
     'g_drawer1': ['g_drawer11']}

    video_annotation = video_annotation_mod.VideoAnnotation(
        '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/Videos/', \
        '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/', \
        bb_to_pddl_obj_dict)


    # ['s13-d25', 's28-d25', 's37-d25', 's21-d21', 's31-d25', 's23-d21', 's13-d21', 's27-d21', 's37-d21', 's22-d25']

    for current_session in video_annotation.session_names:
        detected_added_touches_w_hand_session = []
        possible_actions_session =  []
        detected_added_touches_session = []
        print(current_session)
        video_annotation.create_single_session_dicts(current_session)
        show_annotation(my_parsed_problem, video_annotation, bb_to_pddl_obj_dict, detected_added_touches_w_hand_session, \
                        possible_actions_session, detected_added_touches_session)
        #show_annotation(random.choice(session_names), parsed_problem)
        print(current_session, "done")
        pickle.dump(detected_added_touches_w_hand_session, open("detected_added_touches_w_hand_session_"+str(current_session)+".p", "wb"))
        pickle.dump(possible_actions_session, open("possible_actions_session_"+str(current_session)+".p", "wb"))
        pickle.dump(detected_added_touches_session, open("detected_added_touches_session_"+str(current_session)+".p", "wb"))

if __name__ == "__main__":
    main()