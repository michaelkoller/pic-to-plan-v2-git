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
    (contained ?o)
    (contained_in ?o ?c)
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

(:action put_o1_on_o2
    :parameters (?o1 ?o2)
    :precondition (and (grasped ?o1) (not (stored ?o1)) (not (contained ?o1)) ) ;(not (on_something ?o1))) with this FD exits with -9
	:effect	(and
	            (when (not(container ?o2)) (and (on ?o1 ?o2) (on_something ?o1)))
	            (when (container ?o2) (and (contained_in ?o1 ?o2) (contained ?o1))) )
)

(:action put_o1_away_from_o2
    :parameters (?o1 ?o2)
    :precondition (and (grasped o1))
	:effect	(and
                (when (not(container ?o2)) (and (not(on ?o1 ?o2)) (not(on_something ?o1))))
	            (when (container ?o2) (and (not(contained_in ?o1 ?o2)) (not(contained ?o1))))
            )
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
    :parameters(?o ?k)
    :precondition (and (knife ?k) (grasped ?k) (grasped ?o) (not(stored ?o)) (not(contained ?o)) (washed ?o) (exists (?cb) (and (on ?o ?cb) (cuttingboard ?cb) (not (stored ?cb)))))
    :effect (cut_in_pieces ?o)
)

(:action peel
    :parameters(?o ?p)
    :precondition (and (peeler ?p) (grasped ?p) (grasped ?o) (not(stored ?o)) (not(contained ?o)) )
    :effect (peeled ?o)
)

(:action unstore
    :parameters (?o ?s)
    :precondition (and (storage ?s) (graspable ?o) (stored_in ?o ?s) (open ?s) (not(grasped ?o)))
	:effect	(and (not(stored ?o)) (not(stored_in ?o ?s)))
)

(:action store
    :parameters (?o ?s)
    :precondition (and (not(stored ?o)) (not(stored_in ?o ?s)) (open ?s) (grasped ?o) (storage ?s))
	:effect	(and (stored ?o) (stored_in ?o ?s) (not(grasped ?o))
	            (forall (?h) (when (in_hand ?o ?h) (and (not(in_hand ?o ?h)) (hand_empty ?h))))
	        )
)

(:action open_faucet
    :parameters (?f ?h)
    :precondition (and (faucet ?f) (manipulator ?h))
    :effect (and (faucet_open ?f))
)

(:action wash
    :parameters (?o ?f)
    :precondition (and (faucet ?f) (faucet_open ?f) (grasped ?o) (not(contained ?o)) (not(on_something ?o)) (not(stored ?o))
                  (exists (?h) (and (manipulator ?h) (hand_empty ?h)))
                  )
    :effect (and (washed ?o) (not(faucet_open ?f))) ; describes that you close the faucet after retrieving smthng
)

;end actions

);end domain
