import os
import time

t0 = time.time()
obs_trace_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
print(obs_trace_dir)
os.chdir("/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/")
#os.system("python2 ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G \
#    -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2")


os.execvp("/usr/bin/python", ["/usr/bin/python" ,"/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py",  "-G", \
    "-e", "/home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2"])

os.chdir(obs_trace_dir)
t1 = time.time()
duration = t1 - t0
print(duration)
#TODO why are the different calls to prob_PR.py from this script so much slower than in the terminal?

#Terminal call:
#python ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2
