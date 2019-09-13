(define (domain cut-cucumber)
(:requirements :adl)
(:predicates
    <insert-class-instance-predicates>
    (hand_empty ?x)
    (in_hand ?x ?y)
    (grasped ?o)
    (cut ?o)
    (goaldummy)
)
(:action put_in_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) )
    :effect (and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)))
)
(:action put_out_of_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (in_hand ?o ?h))
	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h) )
)
(:action cut_w_knife
    :parameters(?o ?k)
    :precondition (and (knife ?k) (grasped ?k) (graspable ?o) (grasped ?o))
    :effect (and (cut ?o))
)
)