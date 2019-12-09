import pickle

pos_act = pickle.load(open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_s13-d25.p", "rb"))
count = 1
count2 = 0
distinct_actions = set()
p_a = []
for i, x in enumerate(pos_act):
    #print(i,x)
    for a in x[1]:
        aa = "(" + " ".join(a) + ")"
        p_a.append(aa)
    count *= len(x)
    count2 += len(x)
    for a in x[1]:
        distinct_actions.add(" ".join(a))

print(distinct_actions)
print("distinct actions:", len(distinct_actions))
print("product", count)
print("sum", count2)
print(p_a)

#1,606,938,044,258,990,275,541,962,092,341,162,602,522,202,993,782,792,835,301,376

