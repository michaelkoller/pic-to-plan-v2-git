import os
import collections
file_path = '/media/hdd1/Datasets/GroundingSemanticRoleLabelingForCookingDataset/Video_annotation/Video_annotation/'
output_file_names = []
track_label_file_names = []

all_labels_set = set() #stores all the names of all labels in all videos in the dataset
label_counter_per_video = dict() #stores names and counts of the labels in a specific video
for f in list(os.walk(file_path))[0][2]:
    session_name = f.split(".")[0]
    if "output" in f:
        output_file_names.append(session_name)
    elif "label" in f:
        track_label_file_names.append(session_name)
        with open(file_path + f) as current_track_label_file:
            label_counter_per_video[session_name] = collections.Counter()
            for line in current_track_label_file:
                label = line.split()[1]
                all_labels_set.add(label)
                label_counter_per_video[session_name][label] += 1

print(all_labels_set)
print(len(all_labels_set))
print(label_counter_per_video)
print(output_file_names)
print(track_label_file_names)

with open('/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/labellists_from_video/all_labels_in_video.txt', 'w') as f:
    f.write("\n".join(sorted(list(all_labels_set))))
for name, counter in label_counter_per_video.items():
    with open('/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/labellists_from_video/label_counter_' + name + '.txt', 'w') as f:
        f.write("\n".join(sorted([str(x) + " " + str(counter[x]) for x in counter])))