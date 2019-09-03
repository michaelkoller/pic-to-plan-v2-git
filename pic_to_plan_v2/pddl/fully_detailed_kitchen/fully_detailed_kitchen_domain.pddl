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
(bowl ?o)
	(container ?o)
	(bread ?o)
	(food ?o)
	(graspable ?o)
	(counter ?o)
	(location ?o)
	(cucumber ?o)
	(cucumber_end ?o)
	(waste ?o)
	(cupboard ?o)
	(storage ?o)
	(cuttingboard ?o)
	(tool ?o)
	(drawer ?o)
	(faucet ?o)
	(fridge ?o)
	(hand ?o)
	(manipulator ?o)
	(knife ?o)
	(peel ?o)
	(peeler ?o)
	(plastic_bag ?o)
	(plastic_paper_bag ?o)
	(plate ?o)
	(sink ?o)
	(spice ?o)
	(spice_holder ?o)
	(spice_shaker ?o)
	(sponge ?o)
	(towel ?o)
(hand_empty ?x)
    (in_hand ?x ?y)
    (grasped ?o)
    (open ?s)
    (cut_in_pieces ?o)
    (peeled ?o)
    (stored ?o) ;used to describe that object is not available, because it is still stored somewhere
    (stored_in ?o ?c) ;object is stored in storage
    (on ?x ?y)
    (dummy)
    (washed ?o)
    (faucet_open ?f)
    (contained_in ?o ?c)
    (in_some_container ?o)
    (on_something ?o)
);end predicates

(:action put_in_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) (not (stored ?o)))
	:effect	(and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) )
)

(:action put_out_of_hand
    :parameters (?o ?h)
    :precondition (and (manipulator ?h) (graspable ?o) (in_hand ?o ?h))
	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h))
)

(:action put_object_on
    :parameters (?o1 ?o2 ?h)
    :precondition (and (manipulator ?h) (graspable ?o1) (in_hand ?o1 ?h))
	:effect	(and (when (not(container ?o2)) (and (on ?o1 ?o2) (on_something ?o1)))
	        (when (container ?o2) (and (contained_in ?o1 ?o2) (in_some_container ?o1))))
)

(:action grasp_object_currently_on
    :parameters (?o1 ?o2 ?h)
    :precondition (and (manipulator ?h) (graspable ?o1) (hand_empty ?h) (on ?o1 ?o2))
	:effect	(and (not(on ?o1 ?o2)) (not(hand_empty ?h)) (grasped ?o1) (in_hand ?o1 ?h))
)

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

;(:action cut
;    :parameters(?o ?k)
;    :precondition (and (knife ?k) (grasped ?k) (grasped ?o) (not(stored ?o)))
;    :effect (cut_in_pieces ?o)
;)

(:action cut_on_cuttingboard
    :parameters(?o ?k ?cb)
    :precondition (and (knife ?k) (grasped ?k) (grasped ?o) (on ?o ?cb) (cuttingboard ?cb) (not (stored ?cb))(not(stored ?o)) (washed ?o))
    :effect (cut_in_pieces ?o)
)

(:action peel
    :parameters(?o ?p)
    :precondition (and (peeler ?p) (grasped ?p) (grasped ?o) (not(stored ?o)))
    :effect (peeled ?o)
)

(:action unstore
    :parameters (?o ?h ?s)
    :precondition (and (manipulator ?h) (graspable ?o) (storage ?s) (hand_empty ?h) (not(= ?o ?h)) (not(grasped ?o)) (stored_in ?o ?s) (open ?s))
	:effect	(and (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) (not(stored ?o)) (not(stored_in ?o ?s)))
)

(:action store
    :parameters (?o ?h ?s)
    :precondition (and (manipulator ?h) (graspable ?o) (storage ?s) (not(= ?o ?h))  (in_hand ?o ?h) (grasped ?o) (not (hand_empty ?h)) (not(stored_in ?o ?s)) (open ?s))
	:effect	(and (not(in_hand ?o ?h)) (not(grasped ?o)) (hand_empty ?h) (not(stored ?o)) (stored_in ?o ?s) )
)

(:action open_faucet
    :parameters (?f)
    :precondition (and (faucet ?f))
    :effect (and (faucet_open ?f))
)

(:action wash
    :parameters (?o ?f)
    :precondition (and (faucet ?f) (faucet_open ?f) (not(in_some_container ?o)) (not(on_something ?o)) (not(stored ?o)))
    :effect (and (washed ?o) (not(faucet_open ?f))) ; describes that you close the faucet after retrieving smthng
)

;end actions

);end domain
