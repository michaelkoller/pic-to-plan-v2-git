(define (domain cut-cucumber)
(:requirements :adl)
(:predicates
    <insert-class-instance-predicates>
    (hand_empty ?x)
    (in_hand ?x ?y)
    (grasped ?o)
    (open ?s)
    (cut ?o)
    (stored ?o)
    (stored_in ?o ?s)
    (goaldummy)
)
(:action put_in_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) (not(stored ?o)))
    :effect (and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)))
)
(:action put_out_of_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (in_hand ?o ?h))
	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h) )
)
(:action open_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (location ?s) (hand_empty ?h) (not (open ?s)))
    :effect (and (open ?s) )
)
(:action close_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (location ?s) (hand_empty ?h) (open ?s))
    :effect (and (not(open ?s)))
)
(:action store
    :parameters(?o ?s)
    :precondition (and (graspable ?o) (location ?s) (grasped ?o) (open ?s) (not(stored ?s)))
    :effect (and (stored ?o) (stored_in ?o ?s) (not (grasped ?o)) (forall (?h) (when (grasped ?o) (not(in_hand ?o ?h)))))
)
(:action unstore
    :parameters(?o ?s)
    :precondition (and (graspable ?o) (location ?s) (open ?s) (stored_in ?o ?s))
    :effect (and (not(stored ?o)) (not(stored_in ?o ?s)))
)
    (:action cut_w_knife
    :parameters(?o ?k)
    :precondition (and (knife ?k) (grasped ?k) (food ?o) (grasped ?o))
    :effect (and (cut ?o))
)
)