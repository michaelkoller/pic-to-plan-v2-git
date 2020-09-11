(define
	(domain grounded-CUT-CUCUMBER)
	(:requirements :strips :action-costs)
	(:predicates
		( IN_HAND_BREAD2_L_HAND )
		( GRASPED_BREAD2 )
		( IN_HAND_BREAD2_R_HAND )
		( IN_HAND_BREAD3_L_HAND )
		( GRASPED_BREAD3 )
		( IN_HAND_BREAD3_R_HAND )
		( IN_HAND_END1_L_HAND )
		( GRASPED_END1 )
		( IN_HAND_END1_R_HAND )
		( IN_HAND_PEEL1_L_HAND )
		( GRASPED_PEEL1 )
		( IN_HAND_PEEL1_R_HAND )
		( IN_HAND_TOWEL1_L_HAND )
		( GRASPED_TOWEL1 )
		( IN_HAND_TOWEL1_R_HAND )
		( OPEN_SPICE_HOLDER1 )
		( OPEN_G_DRAWER11 )
		( OPEN_G_DRAWER1 )
		( OPEN_FRIDGE1 )
		( OPEN_DRAWER2 )
		( OPEN_DRAWER1 )
		( OPEN_CUPBOARD1 )
		( STORED_TOWEL1 )
		( STORED_IN_TOWEL1_SPICE_HOLDER1 )
		( STORED_IN_TOWEL1_G_DRAWER11 )
		( STORED_IN_TOWEL1_G_DRAWER1 )
		( STORED_IN_TOWEL1_FRIDGE1 )
		( STORED_IN_TOWEL1_DRAWER2 )
		( STORED_IN_TOWEL1_DRAWER1 )
		( STORED_IN_TOWEL1_CUPBOARD1 )
		( STORED_PEEL1 )
		( STORED_IN_PEEL1_SPICE_HOLDER1 )
		( STORED_IN_PEEL1_G_DRAWER11 )
		( STORED_IN_PEEL1_G_DRAWER1 )
		( STORED_IN_PEEL1_FRIDGE1 )
		( STORED_IN_PEEL1_DRAWER2 )
		( STORED_IN_PEEL1_DRAWER1 )
		( STORED_IN_PEEL1_CUPBOARD1 )
		( STORED_END1 )
		( STORED_IN_END1_SPICE_HOLDER1 )
		( STORED_IN_END1_G_DRAWER11 )
		( STORED_IN_END1_G_DRAWER1 )
		( STORED_IN_END1_FRIDGE1 )
		( STORED_IN_END1_DRAWER2 )
		( STORED_IN_END1_DRAWER1 )
		( STORED_IN_END1_CUPBOARD1 )
		( STORED_BREAD3 )
		( STORED_IN_BREAD3_SPICE_HOLDER1 )
		( STORED_IN_BREAD3_G_DRAWER11 )
		( STORED_IN_BREAD3_G_DRAWER1 )
		( STORED_IN_BREAD3_FRIDGE1 )
		( STORED_IN_BREAD3_DRAWER2 )
		( STORED_IN_BREAD3_DRAWER1 )
		( STORED_IN_BREAD3_CUPBOARD1 )
		( STORED_BREAD2 )
		( STORED_IN_BREAD2_SPICE_HOLDER1 )
		( STORED_IN_BREAD2_G_DRAWER11 )
		( STORED_IN_BREAD2_G_DRAWER1 )
		( STORED_IN_BREAD2_FRIDGE1 )
		( STORED_IN_BREAD2_DRAWER2 )
		( STORED_IN_BREAD2_DRAWER1 )
		( STORED_IN_BREAD2_CUPBOARD1 )
		( NOT-STORED_SPONGE1 )
		( NOT-STORED_SPICE_SHAKER1 )
		( NOT-STORED_SPICE1 )
		( NOT-STORED_PLATE1 )
		( NOT-STORED_PLASTIC_PAPER_BAG1 )
		( NOT-STORED_PLASTIC_BAG1 )
		( NOT-STORED_PEELER1 )
		( NOT-STORED_KNIFE1 )
		( NOT-STORED_CUTTINGBOARD1 )
		( NOT-STORED_CUCUMBER1 )
		( NOT-STORED_BREAD1 )
		( NOT-STORED_BOWL1 )
		( IN_HAND_BOWL1_L_HAND )
		( GRASPED_BOWL1 )
		( IN_HAND_BOWL1_R_HAND )
		( IN_HAND_BREAD1_L_HAND )
		( GRASPED_BREAD1 )
		( IN_HAND_BREAD1_R_HAND )
		( IN_HAND_CUCUMBER1_L_HAND )
		( GRASPED_CUCUMBER1 )
		( IN_HAND_CUCUMBER1_R_HAND )
		( IN_HAND_CUTTINGBOARD1_L_HAND )
		( GRASPED_CUTTINGBOARD1 )
		( IN_HAND_CUTTINGBOARD1_R_HAND )
		( IN_HAND_KNIFE1_L_HAND )
		( GRASPED_KNIFE1 )
		( IN_HAND_KNIFE1_R_HAND )
		( IN_HAND_PEELER1_L_HAND )
		( GRASPED_PEELER1 )
		( IN_HAND_PEELER1_R_HAND )
		( IN_HAND_PLASTIC_BAG1_L_HAND )
		( GRASPED_PLASTIC_BAG1 )
		( IN_HAND_PLASTIC_BAG1_R_HAND )
		( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND )
		( GRASPED_PLASTIC_PAPER_BAG1 )
		( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND )
		( IN_HAND_PLATE1_L_HAND )
		( GRASPED_PLATE1 )
		( IN_HAND_PLATE1_R_HAND )
		( IN_HAND_SPICE1_L_HAND )
		( GRASPED_SPICE1 )
		( IN_HAND_SPICE1_R_HAND )
		( IN_HAND_SPICE_SHAKER1_L_HAND )
		( GRASPED_SPICE_SHAKER1 )
		( IN_HAND_SPICE_SHAKER1_R_HAND )
		( IN_HAND_SPONGE1_L_HAND )
		( GRASPED_SPONGE1 )
		( IN_HAND_SPONGE1_R_HAND )
		( STORED_IN_SPONGE1_SPICE_HOLDER1 )
		( STORED_IN_SPONGE1_G_DRAWER11 )
		( STORED_IN_SPONGE1_FRIDGE1 )
		( STORED_IN_SPONGE1_DRAWER2 )
		( STORED_IN_SPONGE1_DRAWER1 )
		( STORED_IN_SPONGE1_CUPBOARD1 )
		( STORED_IN_SPICE_SHAKER1_G_DRAWER11 )
		( STORED_IN_SPICE_SHAKER1_G_DRAWER1 )
		( STORED_IN_SPICE_SHAKER1_FRIDGE1 )
		( STORED_IN_SPICE_SHAKER1_DRAWER2 )
		( STORED_IN_SPICE_SHAKER1_DRAWER1 )
		( STORED_IN_SPICE_SHAKER1_CUPBOARD1 )
		( STORED_IN_SPICE1_G_DRAWER11 )
		( STORED_IN_SPICE1_G_DRAWER1 )
		( STORED_IN_SPICE1_FRIDGE1 )
		( STORED_IN_SPICE1_DRAWER2 )
		( STORED_IN_SPICE1_DRAWER1 )
		( STORED_IN_SPICE1_CUPBOARD1 )
		( STORED_IN_PLATE1_SPICE_HOLDER1 )
		( STORED_IN_PLATE1_G_DRAWER11 )
		( STORED_IN_PLATE1_G_DRAWER1 )
		( STORED_IN_PLATE1_FRIDGE1 )
		( STORED_IN_PLATE1_DRAWER2 )
		( STORED_IN_PLATE1_DRAWER1 )
		( STORED_IN_PLASTIC_PAPER_BAG1_SPICE_HOLDER1 )
		( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER11 )
		( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER1 )
		( STORED_IN_PLASTIC_PAPER_BAG1_FRIDGE1 )
		( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER2 )
		( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER1 )
		( STORED_IN_PLASTIC_BAG1_SPICE_HOLDER1 )
		( STORED_IN_PLASTIC_BAG1_G_DRAWER11 )
		( STORED_IN_PLASTIC_BAG1_G_DRAWER1 )
		( STORED_IN_PLASTIC_BAG1_FRIDGE1 )
		( STORED_IN_PLASTIC_BAG1_DRAWER2 )
		( STORED_IN_PLASTIC_BAG1_DRAWER1 )
		( STORED_IN_PEELER1_SPICE_HOLDER1 )
		( STORED_IN_PEELER1_G_DRAWER11 )
		( STORED_IN_PEELER1_G_DRAWER1 )
		( STORED_IN_PEELER1_FRIDGE1 )
		( STORED_IN_PEELER1_DRAWER2 )
		( STORED_IN_PEELER1_CUPBOARD1 )
		( STORED_IN_KNIFE1_SPICE_HOLDER1 )
		( STORED_IN_KNIFE1_G_DRAWER11 )
		( STORED_IN_KNIFE1_G_DRAWER1 )
		( STORED_IN_KNIFE1_FRIDGE1 )
		( STORED_IN_KNIFE1_DRAWER2 )
		( STORED_IN_KNIFE1_CUPBOARD1 )
		( STORED_IN_CUTTINGBOARD1_SPICE_HOLDER1 )
		( STORED_IN_CUTTINGBOARD1_G_DRAWER11 )
		( STORED_IN_CUTTINGBOARD1_G_DRAWER1 )
		( STORED_IN_CUTTINGBOARD1_FRIDGE1 )
		( STORED_IN_CUTTINGBOARD1_DRAWER2 )
		( STORED_IN_CUTTINGBOARD1_CUPBOARD1 )
		( STORED_IN_CUCUMBER1_SPICE_HOLDER1 )
		( STORED_IN_CUCUMBER1_G_DRAWER11 )
		( STORED_IN_CUCUMBER1_G_DRAWER1 )
		( STORED_IN_CUCUMBER1_DRAWER2 )
		( STORED_IN_CUCUMBER1_DRAWER1 )
		( STORED_IN_CUCUMBER1_CUPBOARD1 )
		( STORED_IN_BREAD1_SPICE_HOLDER1 )
		( STORED_IN_BREAD1_G_DRAWER11 )
		( STORED_IN_BREAD1_G_DRAWER1 )
		( STORED_IN_BREAD1_FRIDGE1 )
		( STORED_IN_BREAD1_DRAWER2 )
		( STORED_IN_BREAD1_DRAWER1 )
		( STORED_IN_BOWL1_SPICE_HOLDER1 )
		( STORED_IN_BOWL1_G_DRAWER11 )
		( STORED_IN_BOWL1_G_DRAWER1 )
		( STORED_IN_BOWL1_FRIDGE1 )
		( STORED_IN_BOWL1_DRAWER2 )
		( STORED_IN_BOWL1_DRAWER1 )
		( CUT_SPICE1 )
		( CUT_CUCUMBER1 )
		( CUT_BREAD3 )
		( CUT_BREAD2 )
		( CUT_BREAD1 )
		( STORED_BOWL1 )
		( STORED_BREAD1 )
		( STORED_CUCUMBER1 )
		( STORED_CUTTINGBOARD1 )
		( STORED_KNIFE1 )
		( STORED_PEELER1 )
		( STORED_PLASTIC_BAG1 )
		( STORED_PLASTIC_PAPER_BAG1 )
		( STORED_PLATE1 )
		( STORED_SPICE1 )
		( STORED_SPICE_SHAKER1 )
		( STORED_SPONGE1 )
		( NOT-GRASPED_SPONGE1 )
		( HAND_EMPTY_R_HAND )
		( HAND_EMPTY_L_HAND )
		( NOT-GRASPED_SPICE_SHAKER1 )
		( NOT-GRASPED_SPICE1 )
		( NOT-GRASPED_PLATE1 )
		( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
		( NOT-GRASPED_PLASTIC_BAG1 )
		( NOT-GRASPED_PEELER1 )
		( NOT-GRASPED_KNIFE1 )
		( NOT-GRASPED_CUTTINGBOARD1 )
		( NOT-GRASPED_CUCUMBER1 )
		( NOT-GRASPED_BREAD1 )
		( NOT-GRASPED_BOWL1 )
		( STORED_IN_BOWL1_CUPBOARD1 )
		( STORED_IN_BREAD1_CUPBOARD1 )
		( STORED_IN_CUCUMBER1_FRIDGE1 )
		( STORED_IN_CUTTINGBOARD1_DRAWER1 )
		( STORED_IN_KNIFE1_DRAWER1 )
		( STORED_IN_PEELER1_DRAWER1 )
		( STORED_IN_PLASTIC_BAG1_CUPBOARD1 )
		( STORED_IN_PLASTIC_PAPER_BAG1_CUPBOARD1 )
		( STORED_IN_PLATE1_CUPBOARD1 )
		( STORED_IN_SPICE1_SPICE_HOLDER1 )
		( STORED_IN_SPICE_SHAKER1_SPICE_HOLDER1 )
		( STORED_IN_SPONGE1_G_DRAWER1 )
		( NOT-STORED_BREAD2 )
		( NOT-STORED_BREAD3 )
		( NOT-STORED_END1 )
		( NOT-STORED_PEEL1 )
		( NOT-STORED_TOWEL1 )
		( NOT-OPEN_CUPBOARD1 )
		( NOT-OPEN_DRAWER1 )
		( NOT-OPEN_DRAWER2 )
		( NOT-OPEN_FRIDGE1 )
		( NOT-OPEN_G_DRAWER1 )
		( NOT-OPEN_G_DRAWER11 )
		( NOT-OPEN_SPICE_HOLDER1 )
		( NOT-GRASPED_TOWEL1 )
		( NOT-GRASPED_PEEL1 )
		( NOT-GRASPED_END1 )
		( NOT-GRASPED_BREAD3 )
		( NOT-GRASPED_BREAD2 )
		( EXPLAINED_OPEN_STORAGE_WITH_HAND_CUPBOARD1_L_HAND_1 )
		( NOT_EXPLAINED_OPEN_STORAGE_WITH_HAND_CUPBOARD1_L_HAND_1 )
		( EXPLAINED_FULL_OBS_SEQUENCE )
		( NOT_EXPLAINED_FULL_OBS_SEQUENCE )
	) 
	(:functions (total-cost))
	(:action EXPLAIN_OBS_OPEN_STORAGE_WITH_HAND_CUPBOARD1_L_HAND_1
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_CUPBOARD1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_CUPBOARD1 )
			 ( EXPLAINED_OPEN_STORAGE_WITH_HAND_CUPBOARD1_L_HAND_1 )
			 ( EXPLAINED_FULL_OBS_SEQUENCE )
			(not ( NOT-OPEN_CUPBOARD1 ))
			 (not ( NOT_EXPLAINED_OPEN_STORAGE_WITH_HAND_CUPBOARD1_L_HAND_1 ))
			 (not ( NOT_EXPLAINED_FULL_OBS_SEQUENCE ))
		)
	)
	(:action CUT_W_KNIFE_BREAD1_KNIFE1
		:parameters ()
		:precondition
		(and
			( GRASPED_BREAD1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( CUT_BREAD1 )
		)
	)
	(:action CUT_W_KNIFE_BREAD2_KNIFE1
		:parameters ()
		:precondition
		(and
			( GRASPED_BREAD2 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( CUT_BREAD2 )
		)
	)
	(:action CUT_W_KNIFE_BREAD3_KNIFE1
		:parameters ()
		:precondition
		(and
			( GRASPED_BREAD3 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( CUT_BREAD3 )
		)
	)
	(:action CUT_W_KNIFE_CUCUMBER1_KNIFE1
		:parameters ()
		:precondition
		(and
			( GRASPED_CUCUMBER1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( CUT_CUCUMBER1 )
		)
	)
	(:action CUT_W_KNIFE_SPICE1_KNIFE1
		:parameters ()
		:precondition
		(and
			( GRASPED_SPICE1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( CUT_SPICE1 )
		)
	)
	(:action UNSTORE_BOWL1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_DRAWER1 ))
		)
	)
	(:action UNSTORE_BOWL1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_DRAWER2 ))
		)
	)
	(:action UNSTORE_BOWL1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_BOWL1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_BOWL1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_BOWL1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_BREAD1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_DRAWER1 ))
		)
	)
	(:action UNSTORE_BREAD1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_DRAWER2 ))
		)
	)
	(:action UNSTORE_BREAD1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_BREAD1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_BREAD1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_BREAD1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_DRAWER1 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_DRAWER2 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_DRAWER2 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_KNIFE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_KNIFE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_DRAWER2 ))
		)
	)
	(:action UNSTORE_KNIFE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_KNIFE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_KNIFE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_KNIFE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_PEELER1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_PEELER1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_DRAWER2 ))
		)
	)
	(:action UNSTORE_PEELER1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_PEELER1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_PEELER1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_PEELER1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_DRAWER2 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER2 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_PLATE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLATE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_DRAWER2 ))
		)
	)
	(:action UNSTORE_PLATE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_PLATE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLATE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_PLATE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_SPICE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_SPICE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_DRAWER1 ))
		)
	)
	(:action UNSTORE_SPICE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_DRAWER2 ))
		)
	)
	(:action UNSTORE_SPICE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_SPICE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_SPICE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_DRAWER1 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_DRAWER2 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_SPONGE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_SPONGE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_DRAWER1 ))
		)
	)
	(:action UNSTORE_SPONGE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_DRAWER2 ))
		)
	)
	(:action UNSTORE_SPONGE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_SPONGE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_SPONGE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_SPICE_HOLDER1 ))
		)
	)
	(:action STORE_BOWL1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_CUPBOARD1 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BOWL1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_DRAWER1 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BOWL1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_DRAWER2 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BOWL1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_FRIDGE1 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BOWL1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_G_DRAWER1 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BOWL1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_G_DRAWER11 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BOWL1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_BOWL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BOWL1 )
			( STORED_IN_BOWL1_SPICE_HOLDER1 )
			( NOT-GRASPED_BOWL1 )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( NOT-STORED_BOWL1 ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action STORE_BREAD1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_CUPBOARD1 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_BREAD1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_DRAWER1 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_BREAD1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_DRAWER2 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_BREAD1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_FRIDGE1 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_BREAD1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_G_DRAWER1 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_BREAD1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_G_DRAWER11 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_BREAD1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_BREAD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD1 )
			( STORED_IN_BREAD1_SPICE_HOLDER1 )
			( NOT-GRASPED_BREAD1 )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( NOT-STORED_BREAD1 ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action STORE_CUCUMBER1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_CUPBOARD1 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUCUMBER1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_DRAWER1 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUCUMBER1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_DRAWER2 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUCUMBER1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_FRIDGE1 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUCUMBER1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_G_DRAWER1 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUCUMBER1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_G_DRAWER11 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUCUMBER1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_CUCUMBER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUCUMBER1 )
			( STORED_IN_CUCUMBER1_SPICE_HOLDER1 )
			( NOT-GRASPED_CUCUMBER1 )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( NOT-STORED_CUCUMBER1 ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_CUPBOARD1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_DRAWER1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_DRAWER2 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_FRIDGE1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_G_DRAWER1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_G_DRAWER11 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_CUTTINGBOARD1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_CUTTINGBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_CUTTINGBOARD1 )
			( STORED_IN_CUTTINGBOARD1_SPICE_HOLDER1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( NOT-STORED_CUTTINGBOARD1 ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action STORE_KNIFE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_CUPBOARD1 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_KNIFE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_DRAWER1 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_KNIFE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_DRAWER2 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_KNIFE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_FRIDGE1 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_KNIFE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_G_DRAWER1 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_KNIFE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_G_DRAWER11 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_KNIFE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_KNIFE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_KNIFE1 )
			( STORED_IN_KNIFE1_SPICE_HOLDER1 )
			( NOT-GRASPED_KNIFE1 )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( NOT-STORED_KNIFE1 ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action STORE_PEELER1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_CUPBOARD1 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PEELER1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_DRAWER1 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PEELER1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_DRAWER2 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PEELER1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_FRIDGE1 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PEELER1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_G_DRAWER1 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PEELER1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_G_DRAWER11 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PEELER1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_PEELER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEELER1 )
			( STORED_IN_PEELER1_SPICE_HOLDER1 )
			( NOT-GRASPED_PEELER1 )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( NOT-STORED_PEELER1 ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_CUPBOARD1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_DRAWER1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_DRAWER2 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_FRIDGE1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_G_DRAWER1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_G_DRAWER11 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_BAG1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_PLASTIC_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_BAG1 )
			( STORED_IN_PLASTIC_BAG1_SPICE_HOLDER1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_BAG1 ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_CUPBOARD1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_DRAWER2 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_FRIDGE1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_G_DRAWER11 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLASTIC_PAPER_BAG1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_PLASTIC_PAPER_BAG1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLASTIC_PAPER_BAG1 )
			( STORED_IN_PLASTIC_PAPER_BAG1_SPICE_HOLDER1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( NOT-STORED_PLASTIC_PAPER_BAG1 ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action STORE_PLATE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_CUPBOARD1 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_PLATE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_DRAWER1 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_PLATE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_DRAWER2 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_PLATE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_FRIDGE1 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_PLATE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_G_DRAWER1 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_PLATE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_G_DRAWER11 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_PLATE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_PLATE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PLATE1 )
			( STORED_IN_PLATE1_SPICE_HOLDER1 )
			( NOT-GRASPED_PLATE1 )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( NOT-STORED_PLATE1 ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action STORE_SPICE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_CUPBOARD1 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_DRAWER1 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_DRAWER2 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_FRIDGE1 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_G_DRAWER1 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_G_DRAWER11 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_SPICE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE1 )
			( STORED_IN_SPICE1_SPICE_HOLDER1 )
			( NOT-GRASPED_SPICE1 )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( NOT-STORED_SPICE1 ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_CUPBOARD1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_DRAWER1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_DRAWER2 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_FRIDGE1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_G_DRAWER1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_G_DRAWER11 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPICE_SHAKER1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_SPICE_SHAKER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPICE_SHAKER1 )
			( STORED_IN_SPICE_SHAKER1_SPICE_HOLDER1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( NOT-STORED_SPICE_SHAKER1 ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action STORE_SPONGE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_CUPBOARD1 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action STORE_SPONGE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_DRAWER1 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action STORE_SPONGE1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_DRAWER2 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action STORE_SPONGE1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_FRIDGE1 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action STORE_SPONGE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_G_DRAWER1 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action STORE_SPONGE1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_G_DRAWER11 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action STORE_SPONGE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_SPONGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_SPONGE1 )
			( STORED_IN_SPONGE1_SPICE_HOLDER1 )
			( NOT-GRASPED_SPONGE1 )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( NOT-STORED_SPONGE1 ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BOWL1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BOWL1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BOWL1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_BOWL1_L_HAND ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BOWL1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BOWL1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BOWL1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_BOWL1_R_HAND ))
			(not ( GRASPED_BOWL1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BREAD1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BREAD1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BREAD1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_BREAD1_L_HAND ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BREAD1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BREAD1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BREAD1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_BREAD1_R_HAND ))
			(not ( GRASPED_BREAD1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_CUCUMBER1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_CUCUMBER1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_CUCUMBER1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_CUCUMBER1_L_HAND ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_CUCUMBER1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_CUCUMBER1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_CUCUMBER1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_CUCUMBER1_R_HAND ))
			(not ( GRASPED_CUCUMBER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_CUTTINGBOARD1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_CUTTINGBOARD1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_CUTTINGBOARD1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_CUTTINGBOARD1_L_HAND ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_CUTTINGBOARD1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_CUTTINGBOARD1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_CUTTINGBOARD1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_CUTTINGBOARD1_R_HAND ))
			(not ( GRASPED_CUTTINGBOARD1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_KNIFE1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_KNIFE1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_KNIFE1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_KNIFE1_L_HAND ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_KNIFE1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_KNIFE1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_KNIFE1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_KNIFE1_R_HAND ))
			(not ( GRASPED_KNIFE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PEELER1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PEELER1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PEELER1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_PEELER1_L_HAND ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PEELER1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PEELER1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PEELER1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_PEELER1_R_HAND ))
			(not ( GRASPED_PEELER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PLASTIC_BAG1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PLASTIC_BAG1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PLASTIC_BAG1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_PLASTIC_BAG1_L_HAND ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PLASTIC_BAG1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PLASTIC_BAG1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PLASTIC_BAG1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_PLASTIC_BAG1_R_HAND ))
			(not ( GRASPED_PLASTIC_BAG1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PLASTIC_PAPER_BAG1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PLASTIC_PAPER_BAG1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND ))
			(not ( GRASPED_PLASTIC_PAPER_BAG1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PLATE1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PLATE1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PLATE1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_PLATE1_L_HAND ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PLATE1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PLATE1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PLATE1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_PLATE1_R_HAND ))
			(not ( GRASPED_PLATE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_SPICE1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_SPICE1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_SPICE1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_SPICE1_L_HAND ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_SPICE1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_SPICE1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_SPICE1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_SPICE1_R_HAND ))
			(not ( GRASPED_SPICE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_SPICE_SHAKER1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_SPICE_SHAKER1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_SPICE_SHAKER1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_SPICE_SHAKER1_L_HAND ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_SPICE_SHAKER1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_SPICE_SHAKER1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_SPICE_SHAKER1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_SPICE_SHAKER1_R_HAND ))
			(not ( GRASPED_SPICE_SHAKER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_SPONGE1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_SPONGE1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_SPONGE1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_SPONGE1_L_HAND ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_SPONGE1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_SPONGE1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_SPONGE1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_SPONGE1_R_HAND ))
			(not ( GRASPED_SPONGE1 ))
		)
	)
	(:action PUT_IN_HAND_SPONGE1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_SPONGE1 )
			( NOT-GRASPED_SPONGE1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_SPONGE1_R_HAND )
			( GRASPED_SPONGE1 )
			(not ( NOT-GRASPED_SPONGE1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_SPONGE1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_SPONGE1 )
			( NOT-GRASPED_SPONGE1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_SPONGE1_L_HAND )
			( GRASPED_SPONGE1 )
			(not ( NOT-GRASPED_SPONGE1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_SPICE_SHAKER1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_SPICE_SHAKER1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_SPICE_SHAKER1_R_HAND )
			( GRASPED_SPICE_SHAKER1 )
			(not ( NOT-GRASPED_SPICE_SHAKER1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_SPICE_SHAKER1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_SPICE_SHAKER1 )
			( NOT-GRASPED_SPICE_SHAKER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_SPICE_SHAKER1_L_HAND )
			( GRASPED_SPICE_SHAKER1 )
			(not ( NOT-GRASPED_SPICE_SHAKER1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_SPICE1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_SPICE1 )
			( NOT-GRASPED_SPICE1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_SPICE1_R_HAND )
			( GRASPED_SPICE1 )
			(not ( NOT-GRASPED_SPICE1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_SPICE1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_SPICE1 )
			( NOT-GRASPED_SPICE1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_SPICE1_L_HAND )
			( GRASPED_SPICE1 )
			(not ( NOT-GRASPED_SPICE1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_PLATE1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PLATE1 )
			( NOT-GRASPED_PLATE1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PLATE1_R_HAND )
			( GRASPED_PLATE1 )
			(not ( NOT-GRASPED_PLATE1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_PLATE1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PLATE1 )
			( NOT-GRASPED_PLATE1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PLATE1_L_HAND )
			( GRASPED_PLATE1 )
			(not ( NOT-GRASPED_PLATE1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_PLASTIC_PAPER_BAG1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PLASTIC_PAPER_BAG1_R_HAND )
			( GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( NOT-GRASPED_PLASTIC_PAPER_BAG1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_PLASTIC_PAPER_BAG1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			( NOT-GRASPED_PLASTIC_PAPER_BAG1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PLASTIC_PAPER_BAG1_L_HAND )
			( GRASPED_PLASTIC_PAPER_BAG1 )
			(not ( NOT-GRASPED_PLASTIC_PAPER_BAG1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_PLASTIC_BAG1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PLASTIC_BAG1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PLASTIC_BAG1_R_HAND )
			( GRASPED_PLASTIC_BAG1 )
			(not ( NOT-GRASPED_PLASTIC_BAG1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_PLASTIC_BAG1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PLASTIC_BAG1 )
			( NOT-GRASPED_PLASTIC_BAG1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PLASTIC_BAG1_L_HAND )
			( GRASPED_PLASTIC_BAG1 )
			(not ( NOT-GRASPED_PLASTIC_BAG1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_PEELER1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PEELER1 )
			( NOT-GRASPED_PEELER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PEELER1_R_HAND )
			( GRASPED_PEELER1 )
			(not ( NOT-GRASPED_PEELER1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_PEELER1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PEELER1 )
			( NOT-GRASPED_PEELER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PEELER1_L_HAND )
			( GRASPED_PEELER1 )
			(not ( NOT-GRASPED_PEELER1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_KNIFE1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_KNIFE1 )
			( NOT-GRASPED_KNIFE1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_KNIFE1_R_HAND )
			( GRASPED_KNIFE1 )
			(not ( NOT-GRASPED_KNIFE1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_KNIFE1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_KNIFE1 )
			( NOT-GRASPED_KNIFE1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_KNIFE1_L_HAND )
			( GRASPED_KNIFE1 )
			(not ( NOT-GRASPED_KNIFE1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_CUTTINGBOARD1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_CUTTINGBOARD1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_CUTTINGBOARD1_R_HAND )
			( GRASPED_CUTTINGBOARD1 )
			(not ( NOT-GRASPED_CUTTINGBOARD1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_CUTTINGBOARD1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_CUTTINGBOARD1 )
			( NOT-GRASPED_CUTTINGBOARD1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_CUTTINGBOARD1_L_HAND )
			( GRASPED_CUTTINGBOARD1 )
			(not ( NOT-GRASPED_CUTTINGBOARD1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_CUCUMBER1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_CUCUMBER1 )
			( NOT-GRASPED_CUCUMBER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_CUCUMBER1_R_HAND )
			( GRASPED_CUCUMBER1 )
			(not ( NOT-GRASPED_CUCUMBER1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_CUCUMBER1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_CUCUMBER1 )
			( NOT-GRASPED_CUCUMBER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_CUCUMBER1_L_HAND )
			( GRASPED_CUCUMBER1 )
			(not ( NOT-GRASPED_CUCUMBER1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_BREAD1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BREAD1 )
			( NOT-GRASPED_BREAD1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BREAD1_R_HAND )
			( GRASPED_BREAD1 )
			(not ( NOT-GRASPED_BREAD1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_BREAD1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BREAD1 )
			( NOT-GRASPED_BREAD1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BREAD1_L_HAND )
			( GRASPED_BREAD1 )
			(not ( NOT-GRASPED_BREAD1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_BOWL1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BOWL1 )
			( NOT-GRASPED_BOWL1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BOWL1_R_HAND )
			( GRASPED_BOWL1 )
			(not ( NOT-GRASPED_BOWL1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_BOWL1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BOWL1 )
			( NOT-GRASPED_BOWL1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BOWL1_L_HAND )
			( GRASPED_BOWL1 )
			(not ( NOT-GRASPED_BOWL1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action UNSTORE_BOWL1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BOWL1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BOWL1 )
			(not ( STORED_BOWL1 ))
			(not ( STORED_IN_BOWL1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_BREAD1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD1 )
			(not ( STORED_BREAD1 ))
			(not ( STORED_IN_BREAD1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_BREAD2_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_BREAD2_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_DRAWER1 ))
		)
	)
	(:action UNSTORE_BREAD2_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_DRAWER2 ))
		)
	)
	(:action UNSTORE_BREAD2_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_FRIDGE1 ))
		)
	)
	(:action UNSTORE_BREAD2_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_BREAD2_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_BREAD2_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD2_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD2 )
			(not ( STORED_BREAD2 ))
			(not ( STORED_IN_BREAD2_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_BREAD3_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_BREAD3_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_DRAWER1 ))
		)
	)
	(:action UNSTORE_BREAD3_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_DRAWER2 ))
		)
	)
	(:action UNSTORE_BREAD3_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_FRIDGE1 ))
		)
	)
	(:action UNSTORE_BREAD3_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_BREAD3_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_BREAD3_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_BREAD3_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_BREAD3 )
			(not ( STORED_BREAD3 ))
			(not ( STORED_IN_BREAD3_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_CUCUMBER1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUCUMBER1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUCUMBER1 )
			(not ( STORED_CUCUMBER1 ))
			(not ( STORED_IN_CUCUMBER1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_CUTTINGBOARD1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_CUTTINGBOARD1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_CUTTINGBOARD1 )
			(not ( STORED_CUTTINGBOARD1 ))
			(not ( STORED_IN_CUTTINGBOARD1_DRAWER1 ))
		)
	)
	(:action UNSTORE_END1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_END1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_DRAWER1 ))
		)
	)
	(:action UNSTORE_END1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_DRAWER2 ))
		)
	)
	(:action UNSTORE_END1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_END1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_END1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_END1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_END1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_END1 )
			(not ( STORED_END1 ))
			(not ( STORED_IN_END1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_KNIFE1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_KNIFE1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_KNIFE1 )
			(not ( STORED_KNIFE1 ))
			(not ( STORED_IN_KNIFE1_DRAWER1 ))
		)
	)
	(:action UNSTORE_PEEL1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_PEEL1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_DRAWER1 ))
		)
	)
	(:action UNSTORE_PEEL1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_DRAWER2 ))
		)
	)
	(:action UNSTORE_PEEL1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_PEEL1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_PEEL1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_PEEL1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEEL1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEEL1 )
			(not ( STORED_PEEL1 ))
			(not ( STORED_IN_PEEL1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_PEELER1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PEELER1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PEELER1 )
			(not ( STORED_PEELER1 ))
			(not ( STORED_IN_PEELER1_DRAWER1 ))
		)
	)
	(:action UNSTORE_PLASTIC_BAG1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_BAG1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_BAG1 )
			(not ( STORED_PLASTIC_BAG1 ))
			(not ( STORED_IN_PLASTIC_BAG1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_PLASTIC_PAPER_BAG1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLASTIC_PAPER_BAG1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLASTIC_PAPER_BAG1 )
			(not ( STORED_PLASTIC_PAPER_BAG1 ))
			(not ( STORED_IN_PLASTIC_PAPER_BAG1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_PLATE1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_PLATE1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_PLATE1 )
			(not ( STORED_PLATE1 ))
			(not ( STORED_IN_PLATE1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_SPICE1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE1 )
			(not ( STORED_SPICE1 ))
			(not ( STORED_IN_SPICE1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_SPICE_SHAKER1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPICE_SHAKER1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPICE_SHAKER1 )
			(not ( STORED_SPICE_SHAKER1 ))
			(not ( STORED_IN_SPICE_SHAKER1_SPICE_HOLDER1 ))
		)
	)
	(:action UNSTORE_SPONGE1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_SPONGE1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_SPONGE1 )
			(not ( STORED_SPONGE1 ))
			(not ( STORED_IN_SPONGE1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_TOWEL1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_CUPBOARD1 )
			( OPEN_CUPBOARD1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_CUPBOARD1 ))
		)
	)
	(:action UNSTORE_TOWEL1_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_DRAWER1 )
			( OPEN_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_DRAWER1 ))
		)
	)
	(:action UNSTORE_TOWEL1_DRAWER2
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_DRAWER2 )
			( OPEN_DRAWER2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_DRAWER2 ))
		)
	)
	(:action UNSTORE_TOWEL1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_FRIDGE1 )
			( OPEN_FRIDGE1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_FRIDGE1 ))
		)
	)
	(:action UNSTORE_TOWEL1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_G_DRAWER1 )
			( OPEN_G_DRAWER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_G_DRAWER1 ))
		)
	)
	(:action UNSTORE_TOWEL1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_G_DRAWER11 )
			( OPEN_G_DRAWER11 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_G_DRAWER11 ))
		)
	)
	(:action UNSTORE_TOWEL1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( STORED_IN_TOWEL1_SPICE_HOLDER1 )
			( OPEN_SPICE_HOLDER1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-STORED_TOWEL1 )
			(not ( STORED_TOWEL1 ))
			(not ( STORED_IN_TOWEL1_SPICE_HOLDER1 ))
		)
	)
	(:action STORE_BREAD2_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_CUPBOARD1 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD2_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_DRAWER1 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD2_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_DRAWER2 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD2_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_FRIDGE1 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD2_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_G_DRAWER1 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD2_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_G_DRAWER11 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD2_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_BREAD2 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD2 )
			( STORED_IN_BREAD2_SPICE_HOLDER1 )
			( NOT-GRASPED_BREAD2 )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( NOT-STORED_BREAD2 ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action STORE_BREAD3_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_CUPBOARD1 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_BREAD3_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_DRAWER1 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_BREAD3_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_DRAWER2 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_BREAD3_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_FRIDGE1 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_BREAD3_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_G_DRAWER1 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_BREAD3_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_G_DRAWER11 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_BREAD3_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_BREAD3 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_BREAD3 )
			( STORED_IN_BREAD3_SPICE_HOLDER1 )
			( NOT-GRASPED_BREAD3 )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( NOT-STORED_BREAD3 ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action STORE_END1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_CUPBOARD1 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_END1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_DRAWER1 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_END1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_DRAWER2 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_END1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_FRIDGE1 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_END1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_G_DRAWER1 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_END1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_G_DRAWER11 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_END1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_END1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_END1 )
			( STORED_IN_END1_SPICE_HOLDER1 )
			( NOT-GRASPED_END1 )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( IN_HAND_END1_R_HAND ))
			(not ( NOT-STORED_END1 ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action STORE_PEEL1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_CUPBOARD1 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_PEEL1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_DRAWER1 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_PEEL1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_DRAWER2 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_PEEL1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_FRIDGE1 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_PEEL1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_G_DRAWER1 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_PEEL1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_G_DRAWER11 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_PEEL1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_PEEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_PEEL1 )
			( STORED_IN_PEEL1_SPICE_HOLDER1 )
			( NOT-GRASPED_PEEL1 )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( NOT-STORED_PEEL1 ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action STORE_TOWEL1_CUPBOARD1
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_CUPBOARD1 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action STORE_TOWEL1_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_DRAWER1 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action STORE_TOWEL1_DRAWER2
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_DRAWER2 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action STORE_TOWEL1_FRIDGE1
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_FRIDGE1 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action STORE_TOWEL1_G_DRAWER1
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_G_DRAWER1 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action STORE_TOWEL1_G_DRAWER11
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_G_DRAWER11 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action STORE_TOWEL1_SPICE_HOLDER1
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( GRASPED_TOWEL1 )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( STORED_TOWEL1 )
			( STORED_IN_TOWEL1_SPICE_HOLDER1 )
			( NOT-GRASPED_TOWEL1 )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( NOT-STORED_TOWEL1 ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_CUPBOARD1_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_CUPBOARD1 )
			(not ( OPEN_CUPBOARD1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_CUPBOARD1_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_CUPBOARD1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_CUPBOARD1 )
			(not ( OPEN_CUPBOARD1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_DRAWER1_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_DRAWER1 )
			(not ( OPEN_DRAWER1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_DRAWER1_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_DRAWER1 )
			(not ( OPEN_DRAWER1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_DRAWER2_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_DRAWER2 )
			(not ( OPEN_DRAWER2 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_DRAWER2_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_DRAWER2 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_DRAWER2 )
			(not ( OPEN_DRAWER2 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_FRIDGE1_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_FRIDGE1 )
			(not ( OPEN_FRIDGE1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_FRIDGE1_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_FRIDGE1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_FRIDGE1 )
			(not ( OPEN_FRIDGE1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_G_DRAWER1_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_G_DRAWER1 )
			(not ( OPEN_G_DRAWER1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_G_DRAWER1_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_G_DRAWER1 )
			(not ( OPEN_G_DRAWER1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_G_DRAWER11_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_G_DRAWER11 )
			(not ( OPEN_G_DRAWER11 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_G_DRAWER11_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_G_DRAWER11 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_G_DRAWER11 )
			(not ( OPEN_G_DRAWER11 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_SPICE_HOLDER1_L_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_SPICE_HOLDER1 )
			(not ( OPEN_SPICE_HOLDER1 ))
		)
	)
	(:action CLOSE_STORAGE_WITH_HAND_SPICE_HOLDER1_R_HAND
		:parameters ()
		:precondition
		(and
			( OPEN_SPICE_HOLDER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-OPEN_SPICE_HOLDER1 )
			(not ( OPEN_SPICE_HOLDER1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_CUPBOARD1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_CUPBOARD1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_CUPBOARD1 )
			(not ( NOT-OPEN_CUPBOARD1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_DRAWER1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_DRAWER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_DRAWER1 )
			(not ( NOT-OPEN_DRAWER1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_DRAWER1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_DRAWER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_DRAWER1 )
			(not ( NOT-OPEN_DRAWER1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_DRAWER2_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_DRAWER2 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_DRAWER2 )
			(not ( NOT-OPEN_DRAWER2 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_DRAWER2_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_DRAWER2 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_DRAWER2 )
			(not ( NOT-OPEN_DRAWER2 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_FRIDGE1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_FRIDGE1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_FRIDGE1 )
			(not ( NOT-OPEN_FRIDGE1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_FRIDGE1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_FRIDGE1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_FRIDGE1 )
			(not ( NOT-OPEN_FRIDGE1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_G_DRAWER1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_G_DRAWER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_G_DRAWER1 )
			(not ( NOT-OPEN_G_DRAWER1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_G_DRAWER1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_G_DRAWER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_G_DRAWER1 )
			(not ( NOT-OPEN_G_DRAWER1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_G_DRAWER11_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_G_DRAWER11 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_G_DRAWER11 )
			(not ( NOT-OPEN_G_DRAWER11 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_G_DRAWER11_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_G_DRAWER11 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_G_DRAWER11 )
			(not ( NOT-OPEN_G_DRAWER11 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_SPICE_HOLDER1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_SPICE_HOLDER1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_SPICE_HOLDER1 )
			(not ( NOT-OPEN_SPICE_HOLDER1 ))
		)
	)
	(:action OPEN_STORAGE_WITH_HAND_SPICE_HOLDER1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-OPEN_SPICE_HOLDER1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( OPEN_SPICE_HOLDER1 )
			(not ( NOT-OPEN_SPICE_HOLDER1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BREAD2_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BREAD2_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BREAD2 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_BREAD2_L_HAND ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BREAD2_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BREAD2_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BREAD2 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_BREAD2_R_HAND ))
			(not ( GRASPED_BREAD2 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BREAD3_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BREAD3_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BREAD3 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_BREAD3_L_HAND ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action PUT_OUT_OF_HAND_BREAD3_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_BREAD3_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_BREAD3 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_BREAD3_R_HAND ))
			(not ( GRASPED_BREAD3 ))
		)
	)
	(:action PUT_OUT_OF_HAND_END1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_END1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_END1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_END1_L_HAND ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_END1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_END1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_END1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_END1_R_HAND ))
			(not ( GRASPED_END1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PEEL1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PEEL1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PEEL1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_PEEL1_L_HAND ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_PEEL1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_PEEL1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_PEEL1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_PEEL1_R_HAND ))
			(not ( GRASPED_PEEL1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_TOWEL1_L_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_TOWEL1_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_TOWEL1 )
			( HAND_EMPTY_L_HAND )
			(not ( IN_HAND_TOWEL1_L_HAND ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action PUT_OUT_OF_HAND_TOWEL1_R_HAND
		:parameters ()
		:precondition
		(and
			( IN_HAND_TOWEL1_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( NOT-GRASPED_TOWEL1 )
			( HAND_EMPTY_R_HAND )
			(not ( IN_HAND_TOWEL1_R_HAND ))
			(not ( GRASPED_TOWEL1 ))
		)
	)
	(:action PUT_IN_HAND_TOWEL1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_TOWEL1 )
			( NOT-GRASPED_TOWEL1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_TOWEL1_R_HAND )
			( GRASPED_TOWEL1 )
			(not ( NOT-GRASPED_TOWEL1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_TOWEL1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_TOWEL1 )
			( NOT-GRASPED_TOWEL1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_TOWEL1_L_HAND )
			( GRASPED_TOWEL1 )
			(not ( NOT-GRASPED_TOWEL1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_PEEL1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PEEL1 )
			( NOT-GRASPED_PEEL1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PEEL1_R_HAND )
			( GRASPED_PEEL1 )
			(not ( NOT-GRASPED_PEEL1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_PEEL1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_PEEL1 )
			( NOT-GRASPED_PEEL1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_PEEL1_L_HAND )
			( GRASPED_PEEL1 )
			(not ( NOT-GRASPED_PEEL1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_END1_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_END1 )
			( NOT-GRASPED_END1 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_END1_R_HAND )
			( GRASPED_END1 )
			(not ( NOT-GRASPED_END1 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_END1_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_END1 )
			( NOT-GRASPED_END1 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_END1_L_HAND )
			( GRASPED_END1 )
			(not ( NOT-GRASPED_END1 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_BREAD3_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BREAD3 )
			( NOT-GRASPED_BREAD3 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BREAD3_R_HAND )
			( GRASPED_BREAD3 )
			(not ( NOT-GRASPED_BREAD3 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_BREAD3_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BREAD3 )
			( NOT-GRASPED_BREAD3 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BREAD3_L_HAND )
			( GRASPED_BREAD3 )
			(not ( NOT-GRASPED_BREAD3 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)
	(:action PUT_IN_HAND_BREAD2_R_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BREAD2 )
			( NOT-GRASPED_BREAD2 )
			( HAND_EMPTY_R_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BREAD2_R_HAND )
			( GRASPED_BREAD2 )
			(not ( NOT-GRASPED_BREAD2 ))
			(not ( HAND_EMPTY_R_HAND ))
		)
	)
	(:action PUT_IN_HAND_BREAD2_L_HAND
		:parameters ()
		:precondition
		(and
			( NOT-STORED_BREAD2 )
			( NOT-GRASPED_BREAD2 )
			( HAND_EMPTY_L_HAND )
		)
		:effect
		(and
			(increase (total-cost) 1)
			( IN_HAND_BREAD2_L_HAND )
			( GRASPED_BREAD2 )
			(not ( NOT-GRASPED_BREAD2 ))
			(not ( HAND_EMPTY_L_HAND ))
		)
	)

)
