import tarfile
#use this to manually create pr instances
def create_pr_instance(obs, domain_path_inserted_predicates, instance_path_parsed_objects, goal_path):
    print("create plan rec instance:", obs)
    joined_obs = "\n".join(obs)
    obs_file = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/obs.dat", "w")
    obs_file.write(joined_obs)
    obs_file.close()
    #"/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects.pddl",
    instance_template = open(instance_path_parsed_objects, "r")
    template_instance_string = "".join(instance_template.readlines())
    #currently I just replace the (goaldummy) fluent a <HYPOTHESIS>
    # there is a string like <HYPOTHESIS> to replace and the process doesn't break the parse_ontology.py script
    template_instance_string = template_instance_string.replace("(goaldummy)", "<HYPOTHESIS>")
    template_file_pr = open(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/template.pddl", "w")
    template_file_pr.write(template_instance_string)
    template_file_pr.close()

    tar = tarfile.open("sample.tar.bz2", "w:bz2")
    "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl"
    tar.add(domain_path_inserted_predicates, arcname="domain.pddl")
    tar.add(goal_path, arcname="hyps.dat")
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/obs.dat", arcname="obs.dat")
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/pr_test_example/real_hyp.dat", arcname="real_hyp.dat")
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/template.pddl", arcname="template.pddl")
    tar.close()

if __name__ == "__main__":
    #create_pr_instance(["(put_in_hand plate1 r_hand)", "(put_in_hand knife1 r_hand)"], \
                        # "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template_domain.pddl", \
                        # "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/complex-template-instance-parsed-objects.pddl", \
                        # "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/goal_sets/goal_set_used.pddl")

    create_pr_instance(['(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(store plastic_paper_bag1 cupboard1)', '(unstore plastic_paper_bag1 cupboard1)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(store plastic_paper_bag1 cupboard1)', '(unstore plastic_paper_bag1 cupboard1)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(store plate1 cupboard1)', '(unstore plate1 cupboard1)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(store plate1 cupboard1)', '(unstore plate1 cupboard1)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(store plate1 drawer1)', '(unstore plate1 drawer1)', '(store plastic_paper_bag1 drawer1)', '(unstore plastic_paper_bag1 drawer1)', '(open_storage_with_hand drawer1 r_hand)', '(close_storage_with_hand drawer1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(open_storage_with_hand drawer1 l_hand)', '(close_storage_with_hand drawer1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(store knife1 drawer1)', '(unstore knife1 drawer1)', '(store knife1 cupboard1)', '(unstore knife1 cupboard1)', '(open_storage_with_hand drawer1 r_hand)', '(close_storage_with_hand drawer1 r_hand)', '(store knife1 cupboard1)', '(unstore knife1 cupboard1)', '(cut_w_knife bread1 knife1)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(store bread1 drawer1)', '(unstore bread1 drawer1)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(cut_w_knife bread1 knife1)', '(cut_w_knife bread1 knife1)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(store knife1 drawer1)', '(unstore knife1 drawer1)', '(store plastic_paper_bag1 drawer1)', '(unstore plastic_paper_bag1 drawer1)', '(store bread1 drawer1)', '(unstore bread1 drawer1)', '(store plate1 drawer1)', '(unstore plate1 drawer1)', '(open_storage_with_hand drawer1 l_hand)', '(close_storage_with_hand drawer1 l_hand)', '(open_storage_with_hand drawer1 r_hand)', '(close_storage_with_hand drawer1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(store cuttingboard1 drawer1)', '(unstore cuttingboard1 drawer1)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(cut_w_knife bread1 knife1)', '(cut_w_knife bread1 knife1)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(store plastic_paper_bag1 cupboard1)', '(unstore plastic_paper_bag1 cupboard1)'], \
                           "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl", \
                       "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/complex-template-instance-parsed-objects.pddl", \
                       "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/goal_sets/goal_set_used.pddl")

#possible_actions_session_s13-d25.p with complex domain
#['(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(store plastic_paper_bag1 cupboard1)', '(unstore plastic_paper_bag1 cupboard1)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(store plastic_paper_bag1 cupboard1)', '(unstore plastic_paper_bag1 cupboard1)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(store plate1 cupboard1)', '(unstore plate1 cupboard1)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(store plate1 cupboard1)', '(unstore plate1 cupboard1)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(store plate1 drawer1)', '(unstore plate1 drawer1)', '(store plastic_paper_bag1 drawer1)', '(unstore plastic_paper_bag1 drawer1)', '(open_storage_with_hand drawer1 r_hand)', '(close_storage_with_hand drawer1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(open_storage_with_hand drawer1 l_hand)', '(close_storage_with_hand drawer1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(store knife1 drawer1)', '(unstore knife1 drawer1)', '(store knife1 cupboard1)', '(unstore knife1 cupboard1)', '(open_storage_with_hand drawer1 r_hand)', '(close_storage_with_hand drawer1 r_hand)', '(store knife1 cupboard1)', '(unstore knife1 cupboard1)', '(cut_w_knife bread1 knife1)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(store bread1 drawer1)', '(unstore bread1 drawer1)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(cut_w_knife bread1 knife1)', '(cut_w_knife bread1 knife1)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(open_storage_with_hand cupboard1 l_hand)', '(close_storage_with_hand cupboard1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(store knife1 drawer1)', '(unstore knife1 drawer1)', '(store plastic_paper_bag1 drawer1)', '(unstore plastic_paper_bag1 drawer1)', '(store bread1 drawer1)', '(unstore bread1 drawer1)', '(store plate1 drawer1)', '(unstore plate1 drawer1)', '(open_storage_with_hand drawer1 l_hand)', '(close_storage_with_hand drawer1 l_hand)', '(open_storage_with_hand drawer1 r_hand)', '(close_storage_with_hand drawer1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(store cuttingboard1 drawer1)', '(unstore cuttingboard1 drawer1)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(cut_w_knife bread1 knife1)', '(cut_w_knife bread1 knife1)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(cut_w_knife bread1 knife1)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand plastic_paper_bag1 r_hand)', '(put_out_of_hand plastic_paper_bag1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand bread1 r_hand)', '(put_out_of_hand bread1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand plate1 r_hand)', '(put_out_of_hand plate1 r_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plastic_paper_bag1 l_hand)', '(put_out_of_hand plastic_paper_bag1 l_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand bread1 l_hand)', '(put_out_of_hand bread1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand plate1 l_hand)', '(put_out_of_hand plate1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand knife1 l_hand)', '(put_out_of_hand knife1 l_hand)', '(put_in_hand cuttingboard1 r_hand)', '(put_out_of_hand cuttingboard1 r_hand)', '(put_in_hand cuttingboard1 l_hand)', '(put_out_of_hand cuttingboard1 l_hand)', '(put_in_hand knife1 r_hand)', '(put_out_of_hand knife1 r_hand)', '(open_storage_with_hand cupboard1 r_hand)', '(close_storage_with_hand cupboard1 r_hand)', '(store plastic_paper_bag1 cupboard1)', '(unstore plastic_paper_bag1 cupboard1)']
