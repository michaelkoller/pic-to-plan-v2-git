Pic to plan V2
- 
Input
- Kitchen task image sequence
- Ontology about tracked objects
- Planning domain
- Set of goals

Step 1
- Generate observation trace

Step 2
- Perform plan recognition

Step 3 
- HRI, using the perceived observation trace, current state, most likely goal, and plan to achieve said goal


External programs to run:
-
PROBABILISTIC PLAN RECOGNITION
In /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/ :
python ~/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/prob_PR.py -G -e /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test.tar.bz2
where in the planners.py I wrapped the FastDownward planner in lama-first mode for use by the prob-plan-rec script. \
 In hypothesis.py or somewhere like this I changed call to LAMA to a call to FastDownward_LAMA. When not specifying a planner, 
 the FD planner is used. This is good, since the FD planner is also the standard planner for other planning calls in this 
 project.
-G: greedy
-e specify experiment file, must be compressed and contain the structure like in /home/mk/Planning/PlanRecGeffnerRamirez/prob-plan-recognition/block-words_michael_test
 In that file, hyps is the goal set, obs is the observation trace, real_hyp is ground truth and won't be available when 
 running online.
 A call to this delivers a results tar file, where the report.txt tells you which hypothesis (i.e., goal) is the most likely.
 More interestingly, the hyp costs are to be considered, to compare the goals among each other. Don't forget, that for each
 hypothesis, there is one modified planning problem incorporating the observation, and one avoiding the observed actions.
 
 Problem: If the planner cannot reach a goal (for example, if it wants to avoid a certain observed action, but that action is 
 the only way to reach the goal), then the hyp_cost_not is 0.0 (which would be considered cheap and favorable). 
 This in not good, this value should rather be very high, instead of 0.0. 
 
 Maybe the output of the Fast Downward LAMA doesn't set all the necessary output correctly, therefore giving weird plan costs and probabilities
 To look into this, I run the prob-rec and look into log files with the naming scheme pr-problem-0-negO.log
 There the relevant output, if successful is:
 ...
 Solution found!
Actual search time: 0.000328263s [t=0.00191376s]
explain_obs_move_cbs_watson_theater_1  (1) --> where these are the plan steps
activity-take-lecture-1  (1)
move_watson_theater_angazi_cafe  (1)
activity-breakfast  (1)
move_angazi_cafe_hayman_theater  (1)
activity-take-lecture-2  (1)
move_hayman_theater_library  (1)
activity-group-meeting-1  (1)
move_library_tav  (1)
activity-coffee  (1)
Plan length: 10 step(s).
Plan cost: 10
 ...
 So, I changed the costs that are assigned if no solution is found (e.g. 1e2), see planners.py Fastdownward_lama gather_data
 This is ok, but leads to the behavior, that all hypotheses, where O has some cost, and neg_O has cost 100, the
 likelihood expression in line 144 in hypothesis.py leads to 1.0 for all of these hypothesis, and the hypothesis, that
 really is the most likely, must be chosen only by the cost of O (the lower one will be more likely)
 The Hyp_is_True line is just the comparison with the real_hyp, i.e., just a quick string comparison of atoms for checking if 
 result is correct for testing purposes. This line is not the actual result!!
 PRELIM SOLUTION TODO: Just catch all hyps where hyps probability is 1.000, and then take the one with the
 smallest cost for O.
 CATCH: Can I come up with an example, where for a hypothesis O and Neg_O both have plans, but still O should be the most likely
 hypothesis, but is overruled by some hypothesis, that automatically has probability 1.000, because their Neg_0 is very high (i.e., no plan found)?
 Probably, but only if I let the rationality assumption fall! (and that's very relevant)
So, I leave the self.cost = 100 in case there is no plan found in for now.  
 
 Check to recompile the .py files to .pyc in order to have speedup
 
 Attention: the folders called /prob-0-PR/ are created and cleaned up during that call.
 It won't work if these folders exist before the call to prob-PR
 
 #
 FAST DOWNWARD
 The normal planner call:
 /home/mk/Planning/fastdownwardplanner/fast-downward.py  --alias lama-first /home/mk/Planning/PlanRecGeffnerRamirez/aaai-10-benchmarks/block-words-michael-filled-in-problem/domain.pddl /home/mk/Planning/PlanRecGeffnerRamirez/aaai-10-benchmarks/block-words-michael-filled-in-problem/template.pddl

with the --show-aliases keyword you can get more presets, like  --alias seq-sat-lama-2011

# 
VALIDATE 

/home/mk/Planning/VAL/validate -v  /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/current-state-take-put-instance.pddl /home/mk/PycharmProjects/pic-to-plan/current_sas_plan_try

where validate is also installed on the system. 
arguments are a domain, an instance and a plan


-----
TODO maybe it makes sense to push Val, FD and ProbPR also to a git repo so I have a place where I can pull running code...






-----
1: parse ontology
    reads in the ontology and fills in template-domain.pddl and template-instance.pddl as template-domain-inserted-predicates.pddl and 
    template-instance.parsed.objects.pddl
2: watch video
    load the superclass and individual type dict via parse_ontology()
    find all touch events
    find all possible actions
    