import cv2


# ['s13-d25', 's28-d25', 's37-d25', 's21-d21', 's31-d25', 's23-d21', 's13-d21', 's27-d21', 's37-d21', 's22-d25']
# label names from all sessions ['bowl', 'bread', 'counter', 'cucumber', 'cupboard', 'cuttingboard', 'drawer', 'end',
# 'faucet', 'fridge', 'g_drawer', 'knife', 'l_hand', 'peel', 'peeler', 'plastic_bag', 'plastic_paper_bag', 'plate',
# 'r_hand', 'sink', 'spice', 'spice_holder', 'spice_shaker', 'sponge', 'towel']

def show_annotation(frame_dict):
    # read in video and draw annotation
    cap = cv2.VideoCapture("/media/mk/SANDISK/v4r-test-recording/test-video-kitchen-015.mp4")
    current_frame = 0
    font = cv2.FONT_HERSHEY_PLAIN
    startframe = 1185  # start with "startframe", which is in video file name
    while cap.isOpened():
        ret, frame = cap.read()
        # if current_frame - startframe in frame_dict.keys():
        if current_frame in frame_dict.keys():
            current_objects = frame_dict[current_frame]
            for o in current_objects:
                # print(o, current_objects[o])
                cv2.rectangle(frame, (2*current_objects[o][0], 480 - current_objects[o][1]),
                              (2*current_objects[o][2], 480 - current_objects[o][3]), (0, 255, 0), 1)
                # cv2.putText(frame, v_a.label_legend_dict[annotated_obj[0]],
                #            (2 * annotated_obj[1] + 5, 2 * annotated_obj[2] + 15), font, 1, (255, 255, 255), 1,
                #            cv2.LINE_4)

        if not(frame is None):
            cv2.imshow('frame', frame)
            pass
        else:
            cap.release()
            cv2.destroyAllWindows()
        current_frame += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('p'):
            while True:
                if cv2.waitKey(1) & 0xFF == ord('p'):
                    break

    cap.release()
    cv2.destroyAllWindows()


def create_frame_dict():
    path = "/media/mk/SANDISK/v4r-test-recording/output_s08-d02-cam-002_startframe1185.txt"
    frame_dict = {}
    f = open(path, 'r')
    for l in f:
        l = l.strip().split("\t")
        l = [int(x) for x in l]
        if l[5] not in frame_dict:
            frame_dict[l[5]] = {}
        frame_dict[l[5]][l[0]] = [l[i] for i in range(1, 5)]
    return dict


if __name__ == "__main__":
    frame_dict = create_frame_dict()
    show_annotation(frame_dict)