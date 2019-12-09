import pickle
import os
import collections
#/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/results/ComplexDomain100PercentBreadFixed/complex_domain_exp-s13-d21_2019-11-12 13:40:53.510220/in_edge_dict_complex_domain_exp-s13-d21_0.p
#d21 -- cucumber

def evaluate(in_dict_path, out_dict_path, node_dict_path, root_node_path, multiple_in_edges_considered, chosen_set_type):
    #print("LOADING PICKLE FILES")
    in_dict = pickle.load(open(
        in_dict_path, "rb"))
    out_dict = pickle.load(open(
        out_dict_path, "rb"))
    node_dict = pickle.load(open(
        node_dict_path, "rb"))
    root_node = pickle.load(open(
        root_node_path, "rb"))
    #print("LOADED PICKLE FILES")
    in_dict, out_dict, node_dict = get_set(chosen_set_type, root_node, in_dict, out_dict, node_dict)

    val_cuc, val_bread = 0.0, 0.0
    max_cuc, max_bread = 0.0, 0.0
    for n in node_dict.values():
        if len(n.detailed_pr_vals) > 0:
            if multiple_in_edges_considered == True:
                eid_in_set = set()                  #necessary, because the same edges are stored multiple times in given dict key.
                for e in in_dict[n.state_string]:
                    #print(e[1].eid)
                    eid_in_set.add(e[1].eid)
                in_edge_amount = len(eid_in_set)
            #print(n.detailed_pr_vals)
            #assert("cucumber" in n.detailed_pr_vals[0][0], "ERROR, HERE SHOULD BE CUC VAL")
            if "cucumber" in n.detailed_pr_vals[0][0]:
                val_cuc += n.detailed_pr_vals[0][3]
                if n.detailed_pr_vals[0][3] > max_cuc:
                    max_cuc = n.detailed_pr_vals[0][3]
            else:
                print("ERROR, HERE SHOULD BE CUC VAL")
                exit()
            if "bread" in n.detailed_pr_vals[1][0]:
                if multiple_in_edges_considered == True:
                    val_bread += n.detailed_pr_vals[1][3] * in_edge_amount
                else:
                    val_bread += n.detailed_pr_vals[1][3]
                if n.detailed_pr_vals[1][3] > max_bread:
                    max_bread = n.detailed_pr_vals[1][3]
            else:
                print("ERROR, HERE SHOULD BE BREAD VAL")
                exit()
    # print("Result session", s, "(21 = cuc)")
    # print("cuc val", val_cuc)
    # print("bread val", val_bread)
    # print("cuc max", max_cuc)
    # print("bread max", max_bread)
    print("cuc" if "d21" in s else "bread", ",", s,",", round(val_cuc,1),",", round(val_bread, 1),",", round(max_cuc, 3),",", round(max_bread, 3))

def eval_file(results_path, experiment_name, session, use_edges, chosen_set_type):
    directory = os.listdir(results_path + experiment_name + "/")
    instance_name = [x for x in directory if session in x and not ".txt" in x][0]
    #print(instance_name)
    path = results_path + experiment_name + "/" + instance_name + "/"
    max_iter = -1
    root_max_iter = -1
    for r, d, f in os.walk(path):  # find max iter in folder
        for file in f:
            if "out_edge_dict" in file and not ".txt" in file:
                iter = int(str(file).split("_")[-1].split(".")[0])
                max_iter = max(max_iter, iter)
            if "root" in file and not ".txt" in file:
                root_iter = int(str(file).split("_")[-1].split(".")[0])
                root_max_iter = max(root_max_iter, root_iter)

    # # exit()
    #CHANGE WRT ACTUAL INSTANCE NAMES
    # in_dict_path = path + "in_edge_dict_complex_domain_exp-"+session+"_" + str(max_iter) + ".p"
    # out_dict_path = path + "out_edge_dict_complex_domain_exp-"+session+"_" + str(max_iter) + ".p"
    # node_dict_path = path + "node_dict_complex_domain_exp-"+session+"_" + str(max_iter) + ".p"
    # root_node_path = path + "root_node_complex_domain_exp-"+session+"_" + str(root_max_iter) + ".p"
    in_dict_path = path + "in_edge_dict_Cut_bread_and_cucumber_initial_exp-" + session + "_" + str(max_iter) + ".p"
    out_dict_path = path + "out_edge_dict_Cut_bread_and_cucumber_initial_exp-" + session + "_" + str(max_iter) + ".p"
    node_dict_path = path + "node_dict_Cut_bread_and_cucumber_initial_exp-" + session + "_" + str(max_iter) + ".p"
    root_node_path = path + "root_node_Cut_bread_and_cucumber_initial_exp-" + session + "_" + str(root_max_iter) + ".p"
    evaluate(in_dict_path, out_dict_path, node_dict_path, root_node_path, use_edges, chosen_set_type)

def get_set(chosen_set_type, root_node, in_dict, out_dict, node_dict):
    if chosen_set_type == "all":
        return in_dict, out_dict, node_dict
    elif chosen_set_type == "leaf":
        new_node_dict = collections.defaultdict(list)
        for n_key in node_dict.keys():
            if n_key in in_dict and not n_key in out_dict:
                new_node_dict[n_key] = node_dict[n_key]
        return in_dict, out_dict, new_node_dict
    elif chosen_set_type == "single_desc":
        new_node_dict = collections.defaultdict(list)
        new_node_dict[root_node.state_string] = node_dict[root_node.state_string]
        current_edge = root_node.in_edges[0]
        next_edge = None
        while len(current_edge.destination.out_edges) > 0:
            if next_edge is None:
                next_edge = current_edge.destination.out_edges[0]
            for xy in current_edge.destination.out_edges:
                if xy.get_saff_mu(-1) > next_edge.get_saff_mu(-1):
                    next_edge = xy
            new_node_dict[next_edge.destination.state_string] = next_edge.destination
            current_edge = next_edge
            next_edge = None
        return in_dict, out_dict, new_node_dict
        # while len(current_edge.destination.out_edges) > 0:
        #     if next_edge is None:
        #         next_edge = current_edge.destination.out_edges[0]
        #     for xy in current_edge.destination.out_edges:
        #         if xy.saved_saff_mu_val > next_edge.saved_saff_mu_val:
        #             next_edge = xy
        #
        #     new_node_dict[next_edge.destination.state_string] = next_edge.destination
        #     current_edge = next_edge
        #     next_edge = None

        return in_dict, out_dict, node_dict
    elif chosen_set_type == "all_desc":
        return in_dict, out_dict, node_dict

if __name__ == "__main__":
    results_path = "/home/mk/PycharmProjects/pic-to-plan-v2-git/pic_to_plan_v2/data/results/"
    #experiment_name = "ComplexDomain10PercentBreadFixed"
    experiment_name = "CUT-GRASPABLE"

    sessions_cuc = ["s13-d21",
                "s21-d21",
                "s23-d21",
                "s27-d21",
                "s37-d21"]

    sessions_bread = ["s13-d25",
                "s22-d25",
                "s28-d25",
                "s31-d25",
                "s37-d25"]
    #"all", "leaf", "single_desc"
    chosen_set_type = "leaf"
    #whole node set
    for s in sessions_cuc:
        eval_file(results_path, experiment_name, s, False, chosen_set_type)

    for s in sessions_bread:
        eval_file(results_path, experiment_name, s, False, chosen_set_type)

    #while edge set
    for s in sessions_cuc:
        eval_file(results_path, experiment_name, s, True, chosen_set_type)

    for s in sessions_bread:
        eval_file(results_path, experiment_name, s, True, chosen_set_type)