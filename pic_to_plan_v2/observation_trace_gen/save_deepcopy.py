import copy

def save_deepcopy_node(n):
    out_edges = n.out_edges
    in_edges = n.in_edges
    n.out_edges = None
    n.in_edges = None
    new_node = copy.deepcopy(n)
    new_node.out_edges = out_edges
    new_node.in_edges = in_edges
    n.out_edges = out_edges
    n.in_edges = in_edges
    return new_node

def save_deepcopy_edge(e):
    origin = e.origin
    destination = e.destination
    e.origin = None
    e.destination = None
    new_edge = copy.deepcopy(e)
    new_edge.origin = origin
    new_edge.destination = destination
    e.origin = origin
    e.destination = destination
    return new_edge

def save_deepcopy_edges(es):
    new_edges = []
    for e in es:
        new_edges.append(save_deepcopy_edge(e))
    return new_edges
