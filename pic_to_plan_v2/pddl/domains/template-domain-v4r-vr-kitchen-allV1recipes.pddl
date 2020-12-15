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
    (opened_faucet ?o)
    (washed ?o)
    (in ?x ?y)
    (on ?x ?y)
    (goaldummy)
    (cut_cucumber_recipe_done)
    (cut_bread_recipe_done)
    (salad_recipe_done)
    (sandwich_recipe_done)
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

    (:action open_faucet
    :parameters(?m ?f)
    :precondition (and (manipulator ?m) (faucet ?f) (not (opened_faucet ?f)))
    :effect (and (opened_faucet ?f))
)

    (:action wash
    :parameters(?o ?f)
    :precondition (and (grasped ?o) (faucet ?f) (opened_faucet ?f))
    :effect (and (washed ?o))
)

    (:action put_into
    :parameters(?x ?y)
    :precondition (and (grasped ?x) (container ?y))
    :effect (and (in ?x ?y))
)

    (:action put_onto
    :parameters(?x ?y)
    :precondition (and (grasped ?x))
    :effect (and (on ?x ?y))
)

    (:action finish_recipe_cut_cucumber
    :parameters(?o)
    :precondition (and (cucumber ?o) (cut ?o))
    :effect (and (cut_cucumber_recipe_done))
)
    (:action finish_recipe_cut_bread
    :parameters(?o)
    :precondition (and (bread ?o) (cut ?o))
    :effect (and (cut_bread_recipe_done))
)

(:action finish_recipe_sandwich_w_cut_bread
    :parameters(?b ?c ?p1 ?p2)
    :precondition (and (bread ?b) (cut ?b) (cheese ?c) (cut ?c) (produce ?p1) (cut ?p1) (produce ?p2) (cut ?p2) (not (= ?p1 ?p2))
                     (on ?c ?b) (on ?p1 ?b) (on ?p2 ?b) )
    :effect (and (sandwich_recipe_done))
)

(:action finish_recipe_sandwich_w_cut_bread_washed_produce
    :parameters(?b ?c ?p1 ?p2)
    :precondition (and (bread ?b) (cut ?b) (cheese ?c) (cut ?c) (produce ?p1) (cut ?p1) (washed ?p1) (produce ?p2)
                  (washed ?p2) (cut ?p2) (not (= ?p1 ?p2)) (on ?c ?b) (on ?p1 ?b) (on ?p2 ?b) )
    :effect (and (sandwich_recipe_done))
)

(:action finish_recipe_sandwich_w_toast
    :parameters(?b ?c ?p1 ?p2)
    :precondition (and (toast ?b) (cheese ?c) (cut ?c) (produce ?p1) (cut ?p1) (produce ?p2) (cut ?p2)
                    (not (= ?p1 ?p2)) (on ?c ?b) (on ?p1 ?b) (on ?p2 ?b))
    :effect (and (sandwich_recipe_done))
)

(:action finish_recipe_sandwich_w_toast_washed_produce
    :parameters(?b ?c ?p1 ?p2)
    :precondition (and (toast ?b) (cheese ?c) (cut ?c) (produce ?p1) (cut ?p1) (produce ?p2) (cut ?p2)
                    (not (= ?p1 ?p2)) (washed ?p1) (washed ?p2) (on ?c ?b) (on ?p1 ?b) (on ?p2 ?b))
    :effect (and (sandwich_recipe_done))
)

(:action finish_recipe_salad_w_2produce
    :parameters(?b ?p1 ?p2)
    :precondition (and (bowl ?b) (produce ?p1) (cut ?p1) (produce ?p2) (cut ?p2)
                    (not (= ?p1 ?p2)) (in ?p1 ?b) (in ?p2 ?b))
    :effect (and (salad_recipe_done))
)

(:action finish_recipe_salad_w_2produce_washed
    :parameters(?b ?p1 ?p2)
    :precondition (and (bowl ?b) (produce ?p1) (cut ?p1) (produce ?p2) (cut ?p2)
                    (not (= ?p1 ?p2)) (washed ?p1) (washed ?p2) (in ?p1 ?b) (in ?p2 ?b))
    :effect (and (salad_recipe_done))
)
)