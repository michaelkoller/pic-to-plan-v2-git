import tarfile
from pic_to_plan_v2.settings import ROOT_DIR
from pathlib import Path
import os
from ..translate.pddl_parser import lisp_parser
from collections import defaultdict

def traverse_tokens(tokens, add_to_domain_dict):
    traverse_tokens_aux(tokens, add_to_domain_dict)


def traverse_tokens_aux(tokens, add_to_domain_dict):
    for t in tokens:
        if not isinstance(t, str):
            traverse_tokens_aux(t, add_to_domain_dict)
        else:
            #print(t)
            if t == ":predicates":
                tokens.extend(add_to_domain_dict[":predicates"])
            elif t in add_to_domain_dict.keys():
                for o in add_to_domain_dict[t]:
                    if ["p_0"] in o:
                        tokens[7].append("(when (and (= " + tokens[3][0] + " " + o[0][0] + ") " +
                            "(= " + tokens[3][1] + " " + o[0][1] + ")) (p_0))")
                    else:
                        last_index = int(o[1][0].split("_")[-1]) - 1
                        tokens[7].append("(when (and (= " + tokens[3][0] + " " + o[0][0] + ") " +
                            "(= " + tokens[3][1] + " " + o[0][1] + ") (p_" + str(last_index) + ")) (" + o[1][0] +"))")



def untokenize(tokens):
    if isinstance(tokens, str):
        return tokens
    else:
        return "(" + " ".join([untokenize(t) for t in tokens]) +")\n"


def create_pr_instance(obs, domain_path_inserted_predicates, instance_path_parsed_objects, goal_path,  archive_path,
                       archive_name, goal_strings):
    print("create plan rec instance:", obs)
    # add (p_i) fluents to domain
    domain_file = open(domain_path_inserted_predicates, "r")
    tokenized_domain = lisp_parser.parse_nested_list(domain_file)
    add_to_domain_dict = defaultdict(list)
    obs_len = len(obs)
    additional_pr_fluents = [["p_" + str(i)] for i in range(obs_len)]
    add_to_domain_dict[":predicates"] = additional_pr_fluents

    os.system("rm -r " + str(Path(archive_path, archive_name)))
    os.system("mkdir " + str(Path(archive_path, archive_name)))

    for i, observation in enumerate(obs):
        observation = observation[1:-1].split(" ")
        action = observation[0]
        params = observation[1:]
        add_to_domain_dict[action].append([params, additional_pr_fluents[i], i])

    traverse_tokens(tokenized_domain, add_to_domain_dict)

    result = untokenize(tokenized_domain)
    plan_rec_domain = open(Path(archive_path, archive_name, "plan_rec_domain.pddl"), "w")
    plan_rec_domain.write(result)
    plan_rec_domain.close()

    obs_file = open(Path(archive_path, archive_name, "obs.dat"), "w")
    obs_file.write("\n".join(obs))
    obs_file.close()

    goal_file = open(goal_path, "r")
    goals = goal_file.readlines()
    goals = [g.strip() for g in goals]

    instance_file = open(Path(archive_path, archive_name, instance_path_parsed_objects), "r")
    instance_string = "".join(instance_file.readlines())
    for i, goal in enumerate(goals):
        goal_string = goal_strings[i]
        instance_string_w_goal_obs_sat = instance_string
        instance_string_w_goal_obs_sat = instance_string_w_goal_obs_sat.replace("(goaldummy)", goal + " (" + additional_pr_fluents[-1][0] + ")")
        instance_file_w_goal_obs_sat = open(Path(archive_path, archive_name, "plan_rec_instance_" + goal_string + "_obs_sat.pddl"), "w")
        instance_file_w_goal_obs_sat.write(instance_string_w_goal_obs_sat)
        instance_file_w_goal_obs_sat.close()
        instance_string_w_goal_obs_not_sat = instance_string
        instance_string_w_goal_obs_not_sat = instance_string_w_goal_obs_not_sat.replace("(goaldummy)", goal + "(not (" + additional_pr_fluents[-1][0] + "))")
        instance_file_w_goal_obs_not_sat = open(Path(archive_path, archive_name, "plan_rec_instance_" + goal_string + "_obs_not_sat.pddl"), "w")
        instance_file_w_goal_obs_not_sat.write(instance_string_w_goal_obs_not_sat)
        instance_file_w_goal_obs_not_sat.close()
    print("pr instance created")

def create_pr_instance_with_ramirez(obs, domain_path_inserted_predicates, instance_path_parsed_objects, goal_path,  archive_path, archive_name):
    print("create plan rec instance:", obs)
    joined_obs = "\n".join(obs)
    obs_file = Path(ROOT_DIR, "pddl/plan_rec_instances_ramirez/obs.dat").open(mode="w")
    obs_file.write(joined_obs)
    obs_file.close()
    #TODO create unique places to store the created files
    #"/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/instances/template-instance-parsed-objects.pddl",
    instance_template = open(instance_path_parsed_objects, "r")
    template_instance_string = "".join(instance_template.readlines())
    #currently I just replace the (goaldummy) fluent a <HYPOTHESIS>
    # there is a string like <HYPOTHESIS> to replace and the process doesn't break the parse_ontology.py script
    template_instance_string = template_instance_string.replace("(goaldummy)", "<HYPOTHESIS>")
    template_file_pr = Path(ROOT_DIR, "pddl/plan_rec_instances_ramirez/template.pddl").open(mode="w")
    template_file_pr.write(template_instance_string)
    template_file_pr.close()
    tar = tarfile.open(str(archive_path) + os.sep + archive_name + ".tar.bz2", "w:bz2")
    #"/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/pddl/domains/template-domain-inserted-predicates.pddl"
    tar.add(domain_path_inserted_predicates, arcname="domain.pddl")
    tar.add(goal_path, arcname="hyps.dat")
    tar.add(str(Path(ROOT_DIR, "pddl/plan_rec_instances_ramirez/obs.dat")), arcname="obs.dat")
    tar.add(str(Path(ROOT_DIR, "pddl/plan_rec_instances_ramirez/pr_test_example/real_hyp.dat")), arcname="real_hyp.dat")
    tar.add(str(Path(ROOT_DIR, "pddl/plan_rec_instances_ramirez/template.pddl")), arcname="template.pddl")
    tar.close()

if __name__ == "__main__":
    create_pr_instance(["(put_in_hand plastic_paper_bag1 r_hand)"], \
                        str(Path(ROOT_DIR, "pddl/domains/ccb_minimal_template_domain-inserted-predicates.pddl")), \
                        str(Path(ROOT_DIR, "pddl/instances/template-instance-parsed-objects.pddl")), \
                        str(Path(ROOT_DIR, "pddl/goal_sets/goal_set_used.pddl")), \
                        str(Path(ROOT_DIR, "pddl/")), "testpr")
