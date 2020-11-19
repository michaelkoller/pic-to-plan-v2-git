(define (problem cut-cucumber-1)
(:domain cut-cucumber)
(:objects
    bowl1
    bread1
    bread2
    bread3
    counter1
    counter2
    cucumber1
    cupboard1
    cuttingboard1
    drawer1
    drawer2
    end1
    faucet1
    fridge1
    g_drawer1
    g_drawer11
    knife1
    l_hand
    peel1
    peeler1
    plastic_bag1
    plastic_paper_bag1
    plate1
    r_hand
    sink1
    spice1
    spice_holder1
    spice_shaker1
    sponge1
    towel1
)
(:init
    (hand_empty r_hand)  ;put your assumptions about the start of a session here
    (hand_empty l_hand)
    (stored bread1)
    (stored_in bread1 cupboard1)
    (stored plastic_paper_bag1)
    (stored_in plastic_paper_bag1 cupboard1)
    (stored sponge1)
    (stored_in sponge1 g_drawer1)
    (stored peeler1)
    (stored_in peeler1 drawer1)
    (stored cucumber1)
    (stored_in cucumber1 fridge1)
    (stored cuttingboard1)
    (stored_in cuttingboard1 drawer1)
    (stored knife1)
    (stored_in knife1 drawer1)
    (stored plate1)
    (stored_in plate1 cupboard1)
    (stored spice_shaker1)
    (stored_in spice_shaker1 spice_holder1)
    (stored plastic_bag1)
    (stored_in plastic_bag1 cupboard1)
    (stored bowl1)
    (stored_in bowl1 cupboard1)
    (stored spice1)
    (stored_in spice1 spice_holder1)
    (bowl bowl1)
    (container bowl1)
    (graspable bowl1)
    (bread bread1)
    (food bread1)
    (graspable bread1)
    (bread bread2)
    (food bread2)
    (graspable bread2)
    (bread bread3)
    (food bread3)
    (graspable bread3)
    (counter counter1)
    (location counter1)
    (counter counter2)
    (location counter2)
    (cucumber cucumber1)
    (food cucumber1)
    (graspable cucumber1)
    (cupboard cupboard1)
    (storage cupboard1)
    (cuttingboard cuttingboard1)
    (tool cuttingboard1)
    (graspable cuttingboard1)
    (drawer drawer1)
    (storage drawer1)
    (drawer drawer2)
    (storage drawer2)
    (cucumber_end end1)
    (waste end1)
    (graspable end1)
    (faucet faucet1)
    (fridge fridge1)
    (storage fridge1)
    (drawer g_drawer1)
    (storage g_drawer1)
    (drawer g_drawer11)
    (storage g_drawer11)
    (knife knife1)
    (tool knife1)
    (graspable knife1)
    (hand l_hand)
    (manipulator l_hand)
    (peel peel1)
    (waste peel1)
    (graspable peel1)
    (peeler peeler1)
    (tool peeler1)
    (graspable peeler1)
    (plastic_bag plastic_bag1)
    (container plastic_bag1)
    (graspable plastic_bag1)
    (plastic_paper_bag plastic_paper_bag1)
    (container plastic_paper_bag1)
    (graspable plastic_paper_bag1)
    (plate plate1)
    (tool plate1)
    (graspable plate1)
    (hand r_hand)
    (manipulator r_hand)
    (sink sink1)
    (location sink1)
    (spice spice1)
    (food spice1)
    (graspable spice1)
    (spice_holder spice_holder1)
    (storage spice_holder1)
    (spice_shaker spice_shaker1)
    (container spice_shaker1)
    (graspable spice_shaker1)
    (sponge sponge1)
    (tool sponge1)
    (graspable sponge1)
    (towel towel1)
    (tool towel1)
    (graspable towel1)
)
(:goal (and
<HYPOTHESIS>
))
)
