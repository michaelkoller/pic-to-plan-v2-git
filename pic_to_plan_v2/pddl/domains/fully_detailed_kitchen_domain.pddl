;actions:
;put down somewhere
;clean object --> multiple actions probably
;cut --> object needs to be on cuttingboard as precondition
;peel
;retrieve_from_container(object, container)??
;hold tight with other hand
;throw_away_wast
;----
;
;predicates:
;stored(object, container)
;on(object, surface?)
;at_location(object, location)
;at_same_location(o1, o2) --> exists location, st. at_location o1,l, at_location o2, l

;goal: cut cucumber or bread
;not present: waste
;not present: open doors

;s37-d21 --> uses spices on cucumbers!


(define (domain cut-cucumber)
(:requirements :adl)
(:predicates
    <insert-class-instance-predicates>
    (hand_empty ?x)
    (in_hand ?x ?y)
    (grasped ?o)
    (open ?s)
    (cut_in_pieces ?o)
    (stored_in ?o ?c) ;object is stored in container
    (on ?x ?y)
);end predicates

(:action put_in_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) )
	:effect	(and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) )
)

(:action put_out_of_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (in_hand ?o ?h))
	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h))
)

;(:action put_object_on
;    :parameters (?o ?h)
;    :precondition (and (manipulator ?h) (graspable ?o) (in_hand ?o ?h))
;	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h))
;)

(:action open_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (storage ?s) (hand_empty ?h) )
    :effect (and (open ?s))
)

(:action close_storage_with_hand
    :parameters(?s ?h)
    :precondition (and (manipulator ?h) (storage ?s) (hand_empty ?h) )
    :effect (and (not(open ?s)))
)

(:action cut
    :parameters(?o ?k)
    :precondition (and (knife ?k) (grasped ?k) (grasped ?o) )
    :effect (cut_in_pieces ?o)
)

(:action cut
    :parameters(?o ?k ?cb)
    :precondition (and (knife ?k) (grasped ?k) (grasped ?o) (on ?o ?cb))
    :effect (cut_in_pieces ?o)
)

(:action peel
    :parameters(?o ?p)
    :precondition (and (peeler ?p) (grasped ?p) (grasped ?o) )
    :effect (cut_in_pieces ?o)
)


(:action unstore
    :parameters (?o ?h ?c)
    :precondition (and (manipulator ?h) (graspable ?o) (container ?c) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) (stored_in ?o ?c) (open ?c))
	:effect	(and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) (not(stored_in ?o)))
)

(:action store
    :parameters (?o ?h ?c)
    :precondition (and (manipulator ?h) (graspable ?o) (container ?c) (not(= ?o ?h))  (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) (not(stored_in ?o)) (open ?c))
	:effect	(and    (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h) (stored_in ?o ?c) )
)


;end actions

);end domain
