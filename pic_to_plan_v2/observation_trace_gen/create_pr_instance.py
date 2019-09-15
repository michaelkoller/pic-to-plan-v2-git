import tarfile

def create_pr_instance(obs, domain_path_inserted_predicates, instance_path_parsed_objects, goal_path,  archive_path, archive_name):
    print("create plan rec instance:", obs)
    joined_obs = "\n".join(obs)
    obs_file = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/obs.dat", "w")
    obs_file.write(joined_obs)
    obs_file.close()
    #TODO create unique places to store the created files
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

    tar = tarfile.open(archive_path + archive_name + ".tar.bz2", "w:bz2")
    "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl"
    tar.add(domain_path_inserted_predicates, arcname="domain.pddl")
    tar.add(goal_path, arcname="hyps.dat")
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/obs.dat", arcname="obs.dat")
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/pr_test_example/real_hyp.dat", arcname="real_hyp.dat")
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/template.pddl", arcname="template.pddl")
    tar.close()

if __name__ == "__main__":
    create_pr_instance(["(put_in_hand plate1 r_hand)", "(put_in_hand knife1 r_hand)"], \
                        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/ccb_minimal_template_domain.pddl", \
                        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance.pddl", \
                        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/goal_sets/goal_set_used.pddl")
