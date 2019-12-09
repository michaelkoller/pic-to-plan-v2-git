###get all possible storage locations from a possible_actions.p pickle file
#therefore you must have run watch videos before with a domain that has the intended store / unstore actions

import pickle
sessions = ["s13-d21",
    "s13-d25",
    "s21-d21",
    "s22-d25",
    "s23-d21",
    "s27-d21",
    "s28-d25",
    "s31-d25",
    "s37-d21",
    "s37-d25"]

store_set = set()
for sess in sessions:
    overlaps = pickle.load(open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_"+sess+".p", "rb"))
    for l in overlaps:
        for x in l[1]:
            if "store" == x[0]:
                store_set.add(x)
for x in store_set:
    print("(stored " + x[1] + ")")
    print("(stored_in " + x[1] + " "+ x[2]+ ")")
print(len(store_set))