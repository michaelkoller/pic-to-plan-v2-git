import pickle

pos_act = pickle.load(open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/possible_actions/possible_actions_session_s13-d25.p", "rb"))
for i, x in enumerate(pos_act):
    print(i,x)