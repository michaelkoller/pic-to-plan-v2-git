f = open("/media/hdd1/Datasets/MPII-2-Cooking/MPII-Cooking-2/annotation.txt", "r")

print(f.readline())

activity_set = set()
object_set = set()

for l in f:
    l = l.split(",")
    activity_set.add(l[9].strip())
    object_set.add(l[10].strip())
    object_set.add(l[11].strip())
    object_set.add(l[12].strip())
    object_set.add(l[13].strip())
    object_set.add(l[14].strip())
    object_set.add(l[16].strip())
    object_set.add(l[17].strip())

print("\nACTIONS")
activity_list = sorted(list(activity_set))
for x in activity_list:
    print(x)
print(len(activity_list))

print("\nOBJECTS")
object_list = sorted(list(object_set))
for x in object_list:
    print(x)
print(len(object_list))
