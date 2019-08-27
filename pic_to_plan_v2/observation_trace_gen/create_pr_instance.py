import tarfile

def create_pr_instance(obs):
    print("create plan rec instance:", obs)
    joined_obs = "\n".join(obs)
    obs_file = open("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/obs.dat", "w")
    obs_file.write(joined_obs)
    obs_file.close()

    instance_template = open(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects.pddl",
        "r")
    template_instance_string = "".join(instance_template.readlines())
    # TODO currently I just replace the dummy goal (and (grasped cucumber1) (open drawer1)) with a <HYPOTHESIS> make it right later so that
    # there is a string like <HYPOTHESIS> to replace and the process doesn't break the parse_ontology.py script
    template_instance_string = template_instance_string.replace("(grasped cucumber1) (open drawer1)", "<HYPOTHESIS>")
    template_file_pr = open(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/template.pddl", "w")
    template_file_pr.write(template_instance_string)
    template_file_pr.close()

    tar = tarfile.open("sample.tar.bz2", "w:bz2")
    tar.add(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl",
        arcname="domain.pddl")  # ok
    tar.add("/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/goal_sets/goal_set_used.pddl",
            arcname="hyps.dat")  # ok
    tar.add(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/obs.dat",
        arcname="obs.dat")
    tar.add(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/pr_test_example/real_hyp.dat",
        arcname="real_hyp.dat")  # ok
    tar.add(
        "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/plan_rec_instances/template.pddl",
        arcname="template.pddl")  # ok
    tar.close()

if __name__ == "__main__":
    create_pr_instance(["(put_in_hand plate1 r_hand)", "(put_in_hand knife1 r_hand)"])