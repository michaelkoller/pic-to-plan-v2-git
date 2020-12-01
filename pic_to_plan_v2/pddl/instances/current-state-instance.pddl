(define (problem cut-cucumber-1)
(:domain cut-cucumber)
(:objects
    BBQ_1
    apple_1
    apple_2
    avocado_1
    baguette_1
    baguette_2
    baking_paper_1
    balsamic_1
    banana_1
    banana_2
    beer_bottle_1
    beer_can_1
    beer_can_2
    big_plate_1
    big_plate_2
    big_plate_3
    big_plate_4
    big_spoon_1
    bin_1
    black_sesame_1
    blender_body_1
    blender_cap_1
    blueberries_1
    blueberries_2
    bottom_cabinet_1
    bottom_cabinet_2
    bottom_cabinet_3
    bowl_1
    bowl_2
    bowl_3
    bowl_4
    bowl_5
    bowl_6
    bowl_7
    bowl_8
    bowl_9
    bread_loaf_1
    broccoli_1
    bun_1
    butter_1
    can_1
    can_2
    can_3
    can_opener_1
    cap_opener_1
    carrot_1
    cheese_1
    cheese_2
    chocolate_bar_1
    chocolate_bar_2
    cinnamon_1
    cleaver_1
    cocoajar_1
    cocoalid_1
    creole_1
    cucumber_1
    cumin_1
    cup_1
    cup_2
    cutting_board_1
    deep_pan_1
    deep_pan_2
    detergent_1
    dining_table_1
    dishsoap_1
    dough_1
    drawer_1
    egg_1
    egg_2
    egg_3
    egg_cup_glass_1
    egg_cup_glass_2
    espresso_cup_1
    espresso_cup_2
    faucet_1
    flat_dough_1
    floor_1
    flourjar_1
    flourlid_1
    fork_1
    fork_2
    fridge_1
    front_peeler_1
    garlic_1
    garlic_2
    glass_1
    glass_2
    glass_3
    glass_4
    glass_5
    grater_1
    ground_coffee_1
    handsoap_1
    hotsauce_bottle_1
    human_1
    ketchup_bottle_1
    kitchen_knife_1
    kitchen_sink_1
    kitchen_table_1
    kiwi_1
    knife_1
    knife_food_1
    knife_large_1
    knife_large_2
    knife_sharpener_1
    ladle_1
    ladle_2
    large_bowl_1
    large_bowl_2
    lefthand_1
    lemon_1
    lemon_half_1
    lime_1
    lime_half_1
    mais_1
    milk_1
    milkcap_1
    mug_1
    mug_2
    mushroom_1
    mushroom_2
    mushroom_3
    mustard_bottle_1
    olive_oil_1
    onion_1
    onion_2
    orange_1
    orange_2
    orange_half_1
    outlet_1
    outlet_2
    pan_1
    paper_towel_roll_1
    paprika_1
    paprika_powder_1
    pear_1
    pear_2
    pepper_1
    pepper_vegetable_1
    pineapple_1
    pot_1
    pot_2
    pot_top_1
    pot_top_2
    potato_1
    potato_2
    potato_3
    rice_vinegar_1
    righthand_1
    rolling_pin_1
    sage_1
    salad_1
    salad_2
    salad_3
    salt_1
    saucepan_1
    saucepan_big_1
    saucer_1
    saucer_2
    sausage_1
    sausage_2
    sesame_oil_1
    small_plate_1
    small_plate_2
    small_plate_3
    small_plate_4
    small_plate_5
    small_plate_6
    small_plate_7
    smartphone_1
    soy_sauce_1
    spatula_1
    spice_holder_1
    spoon_1
    stove_1
    strawberry_1
    strawberry_2
    strawberry_3
    strawberry_4
    sugarjar_1
    sugarlid_1
    tarragon_1
    tea_cup_1
    tea_cup_2
    tea_pot_1
    tea_pot_cap_1
    thyme_1
    toast_1
    toast_2
    toast_3
    toast_4
    toast_5
    toaster_1
    togarashi_1
    tomato_1
    top_cabinet_1
    top_cabinet_2
    top_cabinet_3
    towel_1
    tray_1
    whisk_1
    white_pepper_1
    white_sesame_1
    wine_glass_1
    wine_glass_2
    worcestershire_sauce_bottle_1
    zucchini_1
)
(:init
    (sauce BBQ_1)
    (food BBQ_1)
    (graspable BBQ_1)
    (apple apple_1)
    (produce apple_1)
    (food apple_1)
    (graspable apple_1)
    (apple apple_2)
    (produce apple_2)
    (food apple_2)
    (graspable apple_2)
    (avocado avocado_1)
    (produce avocado_1)
    (food avocado_1)
    (graspable avocado_1)
    (bread baguette_1)
    (food baguette_1)
    (graspable baguette_1)
    (bread baguette_2)
    (food baguette_2)
    (graspable baguette_2)
    (baking_paper baking_paper_1)
    (tool baking_paper_1)
    (graspable baking_paper_1)
    (vinegar balsamic_1)
    (food balsamic_1)
    (graspable balsamic_1)
    (banana banana_1)
    (produce banana_1)
    (food banana_1)
    (graspable banana_1)
    (banana banana_2)
    (produce banana_2)
    (food banana_2)
    (graspable banana_2)
    (beer beer_bottle_1)
    (food beer_bottle_1)
    (graspable beer_bottle_1)
    (beer beer_can_1)
    (food beer_can_1)
    (graspable beer_can_1)
    (beer beer_can_2)
    (food beer_can_2)
    (graspable beer_can_2)
    (plate big_plate_1)
    (container big_plate_1)
    (graspable big_plate_1)
    (plate big_plate_2)
    (container big_plate_2)
    (graspable big_plate_2)
    (plate big_plate_3)
    (container big_plate_3)
    (graspable big_plate_3)
    (plate big_plate_4)
    (container big_plate_4)
    (graspable big_plate_4)
    (spoon big_spoon_1)
    (tool big_spoon_1)
    (graspable big_spoon_1)
    (bin bin_1)
    (location bin_1)
    (spice black_sesame_1)
    (food black_sesame_1)
    (graspable black_sesame_1)
    (blender blender_body_1)
    (tool blender_body_1)
    (graspable blender_body_1)
    (blender blender_cap_1)
    (tool blender_cap_1)
    (graspable blender_cap_1)
    (blueberries blueberries_1)
    (produce blueberries_1)
    (food blueberries_1)
    (graspable blueberries_1)
    (blueberries blueberries_2)
    (produce blueberries_2)
    (food blueberries_2)
    (graspable blueberries_2)
    (cupboard bottom_cabinet_1)
    (location bottom_cabinet_1)
    (cupboard bottom_cabinet_2)
    (location bottom_cabinet_2)
    (cupboard bottom_cabinet_3)
    (location bottom_cabinet_3)
    (bowl bowl_1)
    (container bowl_1)
    (graspable bowl_1)
    (bowl bowl_2)
    (container bowl_2)
    (graspable bowl_2)
    (bowl bowl_3)
    (container bowl_3)
    (graspable bowl_3)
    (bowl bowl_4)
    (container bowl_4)
    (graspable bowl_4)
    (bowl bowl_5)
    (container bowl_5)
    (graspable bowl_5)
    (bowl bowl_6)
    (container bowl_6)
    (graspable bowl_6)
    (bowl bowl_7)
    (container bowl_7)
    (graspable bowl_7)
    (bowl bowl_8)
    (container bowl_8)
    (graspable bowl_8)
    (bowl bowl_9)
    (container bowl_9)
    (graspable bowl_9)
    (bread bread_loaf_1)
    (food bread_loaf_1)
    (graspable bread_loaf_1)
    (brocolli broccoli_1)
    (produce broccoli_1)
    (food broccoli_1)
    (graspable broccoli_1)
    (bread bun_1)
    (food bun_1)
    (graspable bun_1)
    (butter butter_1)
    (food butter_1)
    (graspable butter_1)
    (can can_1)
    (container can_1)
    (graspable can_1)
    (can can_2)
    (container can_2)
    (graspable can_2)
    (can can_3)
    (container can_3)
    (graspable can_3)
    (can_opener can_opener_1)
    (tool can_opener_1)
    (graspable can_opener_1)
    (cap_opener cap_opener_1)
    (tool cap_opener_1)
    (graspable cap_opener_1)
    (carrot carrot_1)
    (produce carrot_1)
    (food carrot_1)
    (graspable carrot_1)
    (cheese cheese_1)
    (food cheese_1)
    (graspable cheese_1)
    (cheese cheese_2)
    (food cheese_2)
    (graspable cheese_2)
    (chocolate chocolate_bar_1)
    (food chocolate_bar_1)
    (graspable chocolate_bar_1)
    (chocolate chocolate_bar_2)
    (food chocolate_bar_2)
    (graspable chocolate_bar_2)
    (spice cinnamon_1)
    (food cinnamon_1)
    (graspable cinnamon_1)
    (knife cleaver_1)
    (cutting_tool cleaver_1)
    (tool cleaver_1)
    (graspable cleaver_1)
    (chocolate cocoajar_1)
    (food cocoajar_1)
    (graspable cocoajar_1)
    (chocolate cocoalid_1)
    (food cocoalid_1)
    (graspable cocoalid_1)
    (spice creole_1)
    (food creole_1)
    (graspable creole_1)
    (cucumber cucumber_1)
    (produce cucumber_1)
    (food cucumber_1)
    (graspable cucumber_1)
    (spice cumin_1)
    (food cumin_1)
    (graspable cumin_1)
    (cup cup_1)
    (container cup_1)
    (graspable cup_1)
    (cup cup_2)
    (container cup_2)
    (graspable cup_2)
    (cuttingboard cutting_board_1)
    (tool cutting_board_1)
    (graspable cutting_board_1)
    (pan deep_pan_1)
    (container deep_pan_1)
    (graspable deep_pan_1)
    (pan deep_pan_2)
    (container deep_pan_2)
    (graspable deep_pan_2)
    (soap detergent_1)
    (tool detergent_1)
    (graspable detergent_1)
    (counter dining_table_1)
    (location dining_table_1)
    (soap dishsoap_1)
    (tool dishsoap_1)
    (graspable dishsoap_1)
    (dough dough_1)
    (food dough_1)
    (graspable dough_1)
    (drawer drawer_1)
    (location drawer_1)
    (egg egg_1)
    (food egg_1)
    (graspable egg_1)
    (egg egg_2)
    (food egg_2)
    (graspable egg_2)
    (egg egg_3)
    (food egg_3)
    (graspable egg_3)
    (cup egg_cup_glass_1)
    (container egg_cup_glass_1)
    (graspable egg_cup_glass_1)
    (cup egg_cup_glass_2)
    (container egg_cup_glass_2)
    (graspable egg_cup_glass_2)
    (cup espresso_cup_1)
    (container espresso_cup_1)
    (graspable espresso_cup_1)
    (cup espresso_cup_2)
    (container espresso_cup_2)
    (graspable espresso_cup_2)
    (faucet faucet_1)
    (dough flat_dough_1)
    (food flat_dough_1)
    (graspable flat_dough_1)
    (floor floor_1)
    (location floor_1)
    (flour flourjar_1)
    (food flourjar_1)
    (graspable flourjar_1)
    (flour flourlid_1)
    (food flourlid_1)
    (graspable flourlid_1)
    (fork fork_1)
    (tool fork_1)
    (graspable fork_1)
    (fork fork_2)
    (tool fork_2)
    (graspable fork_2)
    (fridge fridge_1)
    (location fridge_1)
    (peeler front_peeler_1)
    (tool front_peeler_1)
    (graspable front_peeler_1)
    (garlic garlic_1)
    (produce garlic_1)
    (food garlic_1)
    (graspable garlic_1)
    (garlic garlic_2)
    (produce garlic_2)
    (food garlic_2)
    (graspable garlic_2)
    (glass glass_1)
    (container glass_1)
    (graspable glass_1)
    (glass glass_2)
    (container glass_2)
    (graspable glass_2)
    (glass glass_3)
    (container glass_3)
    (graspable glass_3)
    (glass glass_4)
    (container glass_4)
    (graspable glass_4)
    (glass glass_5)
    (container glass_5)
    (graspable glass_5)
    (grater grater_1)
    (cutting_tool grater_1)
    (tool grater_1)
    (graspable grater_1)
    (coffee ground_coffee_1)
    (food ground_coffee_1)
    (graspable ground_coffee_1)
    (soap handsoap_1)
    (tool handsoap_1)
    (graspable handsoap_1)
    (sauce hotsauce_bottle_1)
    (food hotsauce_bottle_1)
    (graspable hotsauce_bottle_1)
    (human human_1)
    (sauce ketchup_bottle_1)
    (food ketchup_bottle_1)
    (graspable ketchup_bottle_1)
    (knife kitchen_knife_1)
    (cutting_tool kitchen_knife_1)
    (tool kitchen_knife_1)
    (graspable kitchen_knife_1)
    (sink kitchen_sink_1)
    (location kitchen_sink_1)
    (counter kitchen_table_1)
    (location kitchen_table_1)
    (kiwi kiwi_1)
    (produce kiwi_1)
    (food kiwi_1)
    (graspable kiwi_1)
    (knife knife_1)
    (cutting_tool knife_1)
    (tool knife_1)
    (graspable knife_1)
    (knife knife_food_1)
    (cutting_tool knife_food_1)
    (tool knife_food_1)
    (graspable knife_food_1)
    (knife knife_large_1)
    (cutting_tool knife_large_1)
    (tool knife_large_1)
    (graspable knife_large_1)
    (knife knife_large_2)
    (cutting_tool knife_large_2)
    (tool knife_large_2)
    (graspable knife_large_2)
    (knife_sharpener knife_sharpener_1)
    (tool knife_sharpener_1)
    (graspable knife_sharpener_1)
    (laddle ladle_1)
    (tool ladle_1)
    (graspable ladle_1)
    (laddle ladle_2)
    (tool ladle_2)
    (graspable ladle_2)
    (bowl large_bowl_1)
    (container large_bowl_1)
    (graspable large_bowl_1)
    (bowl large_bowl_2)
    (container large_bowl_2)
    (graspable large_bowl_2)
    (hand lefthand_1)
    (manipulator lefthand_1)
    (lemon lemon_1)
    (produce lemon_1)
    (food lemon_1)
    (graspable lemon_1)
    (lemon lemon_half_1)
    (produce lemon_half_1)
    (food lemon_half_1)
    (graspable lemon_half_1)
    (lime lime_1)
    (produce lime_1)
    (food lime_1)
    (graspable lime_1)
    (lime lime_half_1)
    (produce lime_half_1)
    (food lime_half_1)
    (graspable lime_half_1)
    (mais mais_1)
    (produce mais_1)
    (food mais_1)
    (graspable mais_1)
    (milk milk_1)
    (food milk_1)
    (graspable milk_1)
    (milk milkcap_1)
    (food milkcap_1)
    (graspable milkcap_1)
    (mug mug_1)
    (container mug_1)
    (graspable mug_1)
    (mug mug_2)
    (container mug_2)
    (graspable mug_2)
    (mushroom mushroom_1)
    (produce mushroom_1)
    (food mushroom_1)
    (graspable mushroom_1)
    (mushroom mushroom_2)
    (produce mushroom_2)
    (food mushroom_2)
    (graspable mushroom_2)
    (mushroom mushroom_3)
    (produce mushroom_3)
    (food mushroom_3)
    (graspable mushroom_3)
    (sauce mustard_bottle_1)
    (food mustard_bottle_1)
    (graspable mustard_bottle_1)
    (olive_oil olive_oil_1)
    (food olive_oil_1)
    (graspable olive_oil_1)
    (onion onion_1)
    (produce onion_1)
    (food onion_1)
    (graspable onion_1)
    (onion onion_2)
    (produce onion_2)
    (food onion_2)
    (graspable onion_2)
    (orange orange_1)
    (produce orange_1)
    (food orange_1)
    (graspable orange_1)
    (orange orange_2)
    (produce orange_2)
    (food orange_2)
    (graspable orange_2)
    (orange orange_half_1)
    (produce orange_half_1)
    (food orange_half_1)
    (graspable orange_half_1)
    (outlet outlet_1)
    (tool outlet_1)
    (graspable outlet_1)
    (outlet outlet_2)
    (tool outlet_2)
    (graspable outlet_2)
    (pan pan_1)
    (container pan_1)
    (graspable pan_1)
    (towel paper_towel_roll_1)
    (tool paper_towel_roll_1)
    (graspable paper_towel_roll_1)
    (paprika paprika_1)
    (produce paprika_1)
    (food paprika_1)
    (graspable paprika_1)
    (spice paprika_powder_1)
    (food paprika_powder_1)
    (graspable paprika_powder_1)
    (pear pear_1)
    (produce pear_1)
    (food pear_1)
    (graspable pear_1)
    (pear pear_2)
    (produce pear_2)
    (food pear_2)
    (graspable pear_2)
    (pepper pepper_1)
    (food pepper_1)
    (graspable pepper_1)
    (pepper_vegetable pepper_vegetable_1)
    (produce pepper_vegetable_1)
    (food pepper_vegetable_1)
    (graspable pepper_vegetable_1)
    (pineapple pineapple_1)
    (produce pineapple_1)
    (food pineapple_1)
    (graspable pineapple_1)
    (pot pot_1)
    (container pot_1)
    (graspable pot_1)
    (pot pot_2)
    (container pot_2)
    (graspable pot_2)
    (pot pot_top_1)
    (container pot_top_1)
    (graspable pot_top_1)
    (pot pot_top_2)
    (container pot_top_2)
    (graspable pot_top_2)
    (potato potato_1)
    (produce potato_1)
    (food potato_1)
    (graspable potato_1)
    (potato potato_2)
    (produce potato_2)
    (food potato_2)
    (graspable potato_2)
    (potato potato_3)
    (produce potato_3)
    (food potato_3)
    (graspable potato_3)
    (vinegar rice_vinegar_1)
    (food rice_vinegar_1)
    (graspable rice_vinegar_1)
    (hand righthand_1)
    (manipulator righthand_1)
    (rolling_pin rolling_pin_1)
    (tool rolling_pin_1)
    (graspable rolling_pin_1)
    (spice sage_1)
    (food sage_1)
    (graspable sage_1)
    (salad salad_1)
    (produce salad_1)
    (food salad_1)
    (graspable salad_1)
    (salad salad_2)
    (produce salad_2)
    (food salad_2)
    (graspable salad_2)
    (salad salad_3)
    (produce salad_3)
    (food salad_3)
    (graspable salad_3)
    (salt salt_1)
    (food salt_1)
    (graspable salt_1)
    (pan saucepan_1)
    (container saucepan_1)
    (graspable saucepan_1)
    (pan saucepan_big_1)
    (container saucepan_big_1)
    (graspable saucepan_big_1)
    (saucer saucer_1)
    (container saucer_1)
    (graspable saucer_1)
    (saucer saucer_2)
    (container saucer_2)
    (graspable saucer_2)
    (sausage sausage_1)
    (food sausage_1)
    (graspable sausage_1)
    (sausage sausage_2)
    (food sausage_2)
    (graspable sausage_2)
    (oil sesame_oil_1)
    (food sesame_oil_1)
    (graspable sesame_oil_1)
    (plate small_plate_1)
    (container small_plate_1)
    (graspable small_plate_1)
    (plate small_plate_2)
    (container small_plate_2)
    (graspable small_plate_2)
    (plate small_plate_3)
    (container small_plate_3)
    (graspable small_plate_3)
    (plate small_plate_4)
    (container small_plate_4)
    (graspable small_plate_4)
    (plate small_plate_5)
    (container small_plate_5)
    (graspable small_plate_5)
    (plate small_plate_6)
    (container small_plate_6)
    (graspable small_plate_6)
    (plate small_plate_7)
    (container small_plate_7)
    (graspable small_plate_7)
    (smartphone smartphone_1)
    (tool smartphone_1)
    (graspable smartphone_1)
    (sauce soy_sauce_1)
    (food soy_sauce_1)
    (graspable soy_sauce_1)
    (spatula spatula_1)
    (tool spatula_1)
    (graspable spatula_1)
    (spice_holder spice_holder_1)
    (location spice_holder_1)
    (spoon spoon_1)
    (tool spoon_1)
    (graspable spoon_1)
    (stove stove_1)
    (location stove_1)
    (strawberry strawberry_1)
    (produce strawberry_1)
    (food strawberry_1)
    (graspable strawberry_1)
    (strawberry strawberry_2)
    (produce strawberry_2)
    (food strawberry_2)
    (graspable strawberry_2)
    (strawberry strawberry_3)
    (produce strawberry_3)
    (food strawberry_3)
    (graspable strawberry_3)
    (strawberry strawberry_4)
    (produce strawberry_4)
    (food strawberry_4)
    (graspable strawberry_4)
    (sugar sugarjar_1)
    (food sugarjar_1)
    (graspable sugarjar_1)
    (sugar sugarlid_1)
    (food sugarlid_1)
    (graspable sugarlid_1)
    (spice tarragon_1)
    (food tarragon_1)
    (graspable tarragon_1)
    (cup tea_cup_1)
    (container tea_cup_1)
    (graspable tea_cup_1)
    (cup tea_cup_2)
    (container tea_cup_2)
    (graspable tea_cup_2)
    (tea_pot tea_pot_1)
    (container tea_pot_1)
    (graspable tea_pot_1)
    (tea_pot tea_pot_cap_1)
    (container tea_pot_cap_1)
    (graspable tea_pot_cap_1)
    (spice thyme_1)
    (food thyme_1)
    (graspable thyme_1)
    (bread toast_1)
    (food toast_1)
    (graspable toast_1)
    (bread toast_2)
    (food toast_2)
    (graspable toast_2)
    (bread toast_3)
    (food toast_3)
    (graspable toast_3)
    (bread toast_4)
    (food toast_4)
    (graspable toast_4)
    (bread toast_5)
    (food toast_5)
    (graspable toast_5)
    (toaster toaster_1)
    (tool toaster_1)
    (graspable toaster_1)
    (spice togarashi_1)
    (food togarashi_1)
    (graspable togarashi_1)
    (tomato tomato_1)
    (produce tomato_1)
    (food tomato_1)
    (graspable tomato_1)
    (cupboard top_cabinet_1)
    (location top_cabinet_1)
    (cupboard top_cabinet_2)
    (location top_cabinet_2)
    (cupboard top_cabinet_3)
    (location top_cabinet_3)
    (towel towel_1)
    (tool towel_1)
    (graspable towel_1)
    (tray tray_1)
    (container tray_1)
    (graspable tray_1)
    (whisk whisk_1)
    (tool whisk_1)
    (graspable whisk_1)
    (pepper white_pepper_1)
    (food white_pepper_1)
    (graspable white_pepper_1)
    (spice white_sesame_1)
    (food white_sesame_1)
    (graspable white_sesame_1)
    (glass wine_glass_1)
    (container wine_glass_1)
    (graspable wine_glass_1)
    (glass wine_glass_2)
    (container wine_glass_2)
    (graspable wine_glass_2)
    (sauce worcestershire_sauce_bottle_1)
    (food worcestershire_sauce_bottle_1)
    (graspable worcestershire_sauce_bottle_1)
    (zucchini zucchini_1)
    (produce zucchini_1)
    (food zucchini_1)
    (graspable zucchini_1)
    (stored_in avocado_1 fridge_1) (stored_in butter_1 fridge_1) (stored pot_top_1) (stored kiwi_1) (stored deep_pan_2) (stored glass_5) (stored sugarlid) (stored blueberries_2) (stored milk_1) (stored can_1) (stored_in sesame_oil_1 top_cabinet_2) (stored glass_3) (stored_in flourlid top_cabinet_2) (stored_in bowl_2 fridge_1) (hand_empty r_hand) (stored espresso_cup_1) (stored potato_1) (stored salad_1) (stored_in potato_2 top_cabinet_2) (stored_in garlic_2 top_cabinet_2) (stored_in sugarlid top_cabinet_2) (stored flourjar) (stored_in glass_1 top_cabinet_3) (stored_in orange_1 fridge_1) (stored saucer_2) (stored_in onion_1 top_cabinet_2) (stored faucet_1) (stored pot_2) (stored big_plate_2) (stored_in bowl_9 bowl_8) (stored knife_large_2) (stored_in pot_2 bottom_cabinet_2) (stored_in can_3 top_cabinet_1) (stored_in bowl_7 bottom_cabinet_3) (stored_in ground_coffee_1 bottom_cabinet_1) (stored espresso_cup_2) (stored_in ketchup_bottle_1 top_cabinet_2) (stored_in big_plate_1 top_cabinet_3) (stored handsoap_1) (stored mushroom_1) (stored pepper_vegetable_1) (stored whisk_1) (stored knife_sharpener_1) (stored_in salad_2 fridge_1) (stored_in worcestershire_sauce_bottle_1 top_cabinet_2) (stored pot_1) (stored_in knife_1 drawer_big1) (stored_in knife_food_1 drawer_big1) (stored mug_1) (stored_in cheese_1 fridge_1) (stored lemon_1) (stored_in wine_glass_1 top_cabinet_3) (stored_in cocoalid top_cabinet_2) (stored strawberry_1) (stored beer_bottle_1) (stored_in ladle_2 drawer_big1-2) (stored zucchini_1) (stored salad_3) (stored tray_1) (stored knife_large_1) (stored_in pear_1 fridge_1) (stored_in mug_1 top_cabinet_3) (stored ground_coffee_1) (stored tomato_1) (stored_in deep_pan_1 deep_pan_2) (stored baking_paper_1) (stored bowl_8) (stored_in grater_1 drawer_big1-3) (stored_in blueberries_2 bowl_1) (stored deep_pan_1) (stored front_peeler_1) (stored large_bowl_1) (stored hotsauce_bottle_1) (stored salad_2) (stored_in apple_2 fridge_1) (stored bread_loaf_1) (stored_in lemon_half_1 fridge_1) (stored_in can_opener_1 drawer_big1-1) (stored_in deep_pan_2 bottom_cabinet_2) (stored_in toast_5 top_cabinet_1) (stored milkcap_1) (stored bowl_9) (stored_in strawberry_2 fridge_1) (hand_empty l_hand) (stored_in tea_cup_1 top_cabinet_3) (stored_in bowl_9 bottom_cabinet_3) (stored kitchen_knife_1) (stored_in espresso_cup_2 top_cabinet_3) (stored potato_3) (stored_in glass_2 top_cabinet_3) (stored_in milkcap_1 fridge_1) (stored_in bowl_6 bottom_cabinet_3) (stored can_2) (stored_in olive_oil_1 top_cabinet_2) (stored_in milk_1 fridge_1) (stored_in blender_cap_1 blender_body_1) (stored_in pot_1 bottom_cabinet_2) (stored ketchup_bottle_1) (stored_in big_plate_2 top_cabinet_3) (stored flat_dough_1) (stored baguette_1) (stored_in bowl_3 bottom_cabinet_3) (stored cup_1) (stored_in dough_1 fridge_1) (stored small_plate_6) (stored_in flourjar top_cabinet_2) (stored_in fork_2 drawer_big1) (stored_in pot_top_2 bottom_cabinet_2) (stored_in egg_cup_glass_1 top_cabinet_3) (stored toast_3) (stored_in salad_3 fridge_1) (stored_in saucer_1 top_cabinet_3) (stored egg_2) (stored egg_cup_glass_1) (stored_in egg_1 fridge_1) (stored_in ladle_1 drawer_big1-5) (stored lime_1) (stored sausage_2) (stored_in large_bowl_1 large_bowl_2) (stored ladle_2) (stored egg_1) (stored_in potato_3 top_cabinet_2) (stored knife_food_1) (stored mug_2) (stored_in cleaver_1 drawer_big1-1) (stored ladle_1) (stored bowl_4) (stored blueberries_1) (stored_in rice_vinegar_1 top_cabinet_2) (stored dishsoap_1) (stored_in mug_2 top_cabinet_3) (stored_in banana_2 fridge_1) (stored_in kitchen_knife_1 drawer_big1-1) (stored_in cutting_board_1 drawer_big1-3) (stored_in espresso_cup_1 top_cabinet_3) (stored_in flat_dough_1 fridge_1) (stored knife_1) (stored_in detergent_1 kitchen_sink_1) (stored glass_2) (stored_in wine_glass_2 top_cabinet_3) (stored mushroom_2) (stored lime_half_1) (stored_in cap_opener_1 drawer_big1-1) (stored_in bowl_8 bowl_9) (stored_in zucchini_1 fridge_1) (stored_in baguette_1 top_cabinet_1) (stored strawberry_3) (stored wine_glass_2) (stored pear_2) (stored_in banana_1 fridge_1) (stored egg_3) (stored_in lime_1 fridge_1) (stored_in bowl_8 bottom_cabinet_3) (stored_in pepper_vegetable_1 fridge_1) (stored_in cheese_2 fridge_1) (stored onion_1) (stored rolling_pin_1) (stored tea_cup_2) (stored_in mushroom_3 fridge_1) (stored_in bun_1 top_cabinet_1) (stored_in knife_sharpener_1 drawer_big1-1) (stored baguette_2) (stored_in mushroom_1 fridge_1) (stored_in small_plate_5 top_cabinet_1) (stored_in large_bowl_2 bottom_cabinet_3) (stored_in strawberry_3 fridge_1) (stored_in saucepan_1 bottom_cabinet_2) (stored detergent_1) (stored beer_can_2) (stored_in blueberries_2 fridge_1) (stored toast_5) (stored can_3) (stored big_plate_1) (stored_in soy_sauce_1 top_cabinet_2) (stored strawberry_2) (stored_in tea_pot_cap_1 bottom_cabinet_1) (stored banana_1) (stored_in knife_large_2 drawer_big1-1) (stored cucumber_1) (stored_in egg_cup_glass_2 top_cabinet_3) (stored big_spoon_1) (stored grater_1) (stored cocoajar) (stored glass_1) (stored_in large_bowl_1 bottom_cabinet_3) (stored bun_1) (stored blender_cap_1) (stored_in mushroom_2 fridge_1) (stored_in salad_1 fridge_1) (stored_in toast_4 top_cabinet_1) (stored sugarjar) (stored cheese_2) (stored can_opener_1) (stored garlic_2) (stored_in strawberry_4 fridge_1) (stored_in small_plate_6 fridge_1) (stored_in sugarjar top_cabinet_2) (stored egg_cup_glass_2) (stored orange_1) (stored olive_oil_1) (stored pot_top_2) (stored_in baguette_2 top_cabinet_1) (stored_in egg_2 fridge_1) (stored_in pear_2 fridge_1) (stored_in tray_1 stove_1) (stored mustard_bottle_1) (stored bowl_5) (stored_in garlic_1 top_cabinet_2) (stored_in hotsauce_bottle_1 top_cabinet_2) (stored pear_1) (stored_in fork_1 drawer_big1) (stored saucepan_1) (stored large_bowl_2) (stored_in cocoajar top_cabinet_2) (stored_in cucumber_1 fridge_1) (stored_in cup_1 top_cabinet_3) (stored cleaver_1) (stored garlic_1) (stored_in pineapple_1 fridge_1) (stored_in rolling_pin_1 drawer_big1-2) (stored_in orange_2 fridge_1) (stored_in tea_cup_2 top_cabinet_3) (stored bowl_6) (stored_in glass_4 top_cabinet_3) (stored_in whisk_1 drawer_big1-2) (stored_in bowl_6 bowl_7) (stored_in saucepan_big_1 bottom_cabinet_2) (stored dough_1) (stored_in toast_2 top_cabinet_1) (stored fork_2) (stored_in carrot_1 fridge_1) (stored_in beer_can_1 fridge_1) (stored onion_2) (stored toast_1) (stored bowl_7) (stored_in kiwi_1 fridge_1) (stored_in blueberries_1 fridge_1) (stored_in tomato_1 fridge_1) (stored worcestershire_sauce_bottle_1) (stored_in tea_pot_cap_1 tea_pot_1) (stored avocado_1) (stored_in faucet_1 kitchen_sink_1) (stored_in can_2 top_cabinet_1) (stored orange_half_1) (stored sausage_1) (stored balsamic_1) (stored_in onion_2 top_cabinet_2) (stored carrot_1) (stored pineapple_1) (stored_in balsamic_1 top_cabinet_2) (stored_in potato_1 top_cabinet_2) (stored_in pot_top_1 bottom_cabinet_2) (stored beer_can_1) (stored_in can_1 top_cabinet_1) (stored_in broccoli_1 fridge_1) (stored_in knife_large_1 drawer_big1) (stored banana_2) (stored_in beer_bottle_1 fridge_1) (stored strawberry_4) (stored_in bowl_4 bottom_cabinet_3) (stored_in cup_2 top_cabinet_3) (stored fork_1) (stored saucer_1) (stored cheese_1) (stored butter_1) (stored_in glass_5 top_cabinet_3) (stored_in sausage_1 fridge_1) (stored_in glass_3 top_cabinet_3) (stored_in egg_3 fridge_1) (stored_in big_spoon_1 drawer_big1-2) (stored_in baking_paper_1 bottom_cabinet_1) (stored mushroom_3) (stored_in front_peeler_1 drawer_big1-1) (stored_in lime_half_1 fridge_1) (stored rice_vinegar_1) (stored_in deep_pan_1 bottom_cabinet_2) (stored cocoalid) (stored_in toast_1 top_cabinet_1) (stored_in orange_half_1 fridge_1) (stored glass_4) (stored_in lemon_1 fridge_1) (stored toast_2) (stored cap_opener_1) (stored saucepan_big_1) (stored_in handsoap_1 kitchen_sink_1) (stored_in sausage_2 fridge_1) (stored apple_2) (stored_in strawberry_1 fridge_1) (stored_in spoon_1 drawer_big1) (stored wine_glass_1) (stored cutting_board_1) (stored_in beer_can_2 fridge_1) (stored small_plate_5) (stored orange_2) (stored_in toast_3 top_cabinet_1) (stored_in bread_loaf_1 top_cabinet_1) (stored_in bowl_5 bottom_cabinet_3) (stored_in saucer_2 top_cabinet_3) (stored toast_4) (stored bowl_2) (stored tea_pot_cap_1) (stored_in dishsoap_1 kitchen_sink_1) (stored_in mustard_bottle_1 top_cabinet_2) (stored bowl_3) (stored soy_sauce_1) (stored lemon_half_1) (stored potato_2) (stored spoon_1) (stored flourlid) (stored tea_cup_1) (stored broccoli_1) (stored cup_2) (stored sesame_oil_1)
)
(:goal (and
(goaldummy)
))
)
