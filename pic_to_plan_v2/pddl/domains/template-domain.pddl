(define (domain cut-cucumber)
(:requirements :adl)
(:predicates
    <insert-class-instance-predicates>
    (hand_empty ?x)
    (in_hand ?x ?y)
    (grasped ?o)
    (open ?s)
    (used ?o)
    (active ?o )
);end predicates

(:action put_in_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) )
	:effect	(and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) (used ?o) (active ?o))
)

(:action put_out_of_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (in_hand ?o ?h))
	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h) (used ?o) (active ?o))
)

(:action open_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (storage ?s) (hand_empty ?h) )
    :effect (and (open ?s) (used ?s) (active ?s))
)

(:action close_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (storage ?s) (hand_empty ?h) )
    :effect (and (not(open ?s)) (used ?s) (active ?o))
)

(:action cut
    :parameters(?o ?k)
    :precondition (and (knife ?k) (exists (?h) (and (manipulator ?h) (in_hand ?k ?h))))
    :effect (active ?o)
)
;end actions

);end domain


; in ~/Planning/fastdownwardplanner, run
; ./fast-downward.py /home/mk/PycharmProjects/pic-to-plan/take-put-domain.pddl /home/mk/PycharmProjects/pic-to-plan/take-put-instance.pddl --search "astar(lmcut())"
; in a terminal
; in that folder, sas_plan is the plan output


;VALIDATE doesn't work if an action has no preconditions specified