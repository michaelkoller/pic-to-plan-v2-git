(define (domain cut-cucumber)
(:requirements :adl)
(:predicates
    <insert-class-instance-predicates>
    (hand_empty ?x)
    (in_hand ?x ?y)
    (grasped ?o)
    (open ?s)
    (cut ?o)
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
(:action open_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (storage ?s) (hand_empty ?h) (not (open ?s)))
    :effect (and (open ?s) )
)
(:action close_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (storage ?s) (hand_empty ?h) (open ?s))
    :effect (and (not(open ?s)))
)
(:action cut_w_knife
    :parameters(?o ?k)
    :precondition (and (knife ?k) (grasped ?k) (food ?o) (grasped ?o))
    :effect (and (cut ?o))
)
)