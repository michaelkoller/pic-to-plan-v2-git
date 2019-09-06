(define (problem cut-cucumber-1)
(:domain cut-cucumber)
(:objects
    <insert_objects>
)
(:init
    (hand_empty r_hand)  ;put your assumptions about the start of a session here
    (hand_empty l_hand)
    <insert_class_memberships>
)
(:goal (and
(grasped cucumber1) (open drawer1)
))
)
