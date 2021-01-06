import os
import time
import numpy as np
import pickle
#os.chdir("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/prob-plan-recognition-5")
#os.chdir("/usr/bin/python /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/prob-plan-recognition-7/prob_PR.py -G -e /home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances_ramirez/pr_instance_7.tar.bz2")

#cmd_string = '/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/fd-5/fast-downward.py results/prob-1-PR/O/pr-domain.pddl results/prob-1-PR/O/pr-problem.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"'
cmd_string = '/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/fd-5/fast-downward.py results/prob-1-PR/O/pr-domain.pddl results/prob-1-PR/O/pr-problem.pddl '
repeats_per_config = 5
#http://www.fast-downward.org/PlannerUsage
#http://www.fast-downward.org/IpcPlanners
configs = ['--evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"',
           '--evaluator "hff=ff()" --search "lazy_greedy([hff], preferred=[hff])"',
           '--evaluator "hcea=cea()" --search "lazy_greedy([hcea], preferred=[hcea])"',
           '--search "astar(lmcut())"',
           '--search "astar(ipdb())"',
           '--search "astar(blind())"',
           '--alias seq-sat-lama-2011',
            '--alias lama',
            '--alias lama-first',
            '--alias seq-opt-bjolp',
            '--alias seq-opt-fdss-1',
            '--alias seq-opt-fdss-2',
            '--alias seq-opt-lmcut',
            '--alias seq-opt-merge-and-shrink',
            '--alias seq-sat-fd-autotune-1',
            '--alias seq-sat-fd-autotune-2',
            '--alias seq-sat-fdss-1',
            '--alias seq-sat-fdss-2',
            '--alias seq-sat-fdss-2014',
            '--alias seq-sat-lama-2011',
           ]
config_stats = np.zeros((len(configs), repeats_per_config))

for c_no, config in enumerate(configs):
    try:
        for i in range(repeats_per_config):
            t_0 = time.time()
            os.system(cmd_string + config)
            t_1 = time.time()
            config_stats[c_no][i] = t_1 - t_0
    except:
        print("ERROR IN", config)

print(config_stats)
pickle.dump( config_stats, open( "config_stats.p", "wb" ) )

config_stats.mean(axis=1)

