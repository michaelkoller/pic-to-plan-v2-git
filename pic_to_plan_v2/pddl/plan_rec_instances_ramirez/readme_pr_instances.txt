Each Plan Rec Instance needs to have the following files:

domain.pddl
    This is the normal domain model. (template-domain-inserted-predicates.pddl)
hyps.dat
    This is the goal set. (goal_set_used.pddl)
obs.dat
    This is the observation trace. Create this dyanamically for each node in the search tree by
    going up the path to root and pre-appending all non-"nop" actions
real_hyp.dat
    Put the correct goal here. #TODO this won't be available of course in a real-world example.
    Check out what you minimally need to put into this file. So far I only see that in the "report.txt"
    file is sets Hyp_Is_True=True or Hyp_Is_True=False to easily see what the true goal among all
    hypotheses was.
template.pddl
    This is the instance, with the assumed init state and objects, but with
    "(and <HYPOTHESIS>))" as goal. prob_PR inserts all goal in the goal set here.