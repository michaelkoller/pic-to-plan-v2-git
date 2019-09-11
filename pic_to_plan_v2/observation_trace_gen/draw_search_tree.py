import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

def draw_tree_nx(G, name, current_results_dir):
    # write dot file to use with graphviz
    # run "dot -Tpng test.dot >test.png"
    write_dot(G,current_results_dir + '/nx_' + str(name) + '.dot')

    # same layout using matplotlib with no labels
    plt.title(name)
    pos =graphviz_layout(G, prog='dot')
    plt.figure(1, figsize=(1200, 1200))
    nx.draw(G, pos, with_labels=False, arrows=True, node_size=1)
    plt.savefig(current_results_dir +'/nx_' + str(name) + '.png')
    plt.show()


if __name__ == "__main__":
    G = nx.DiGraph()

    G.add_node("ROOT")

    for i in range(5):
        G.add_node("Child_%i" % i)
        G.add_node("Grandchild_%i" % i)
        G.add_node("Greatgrandchild_%i" % i)

        G.add_edge("ROOT", "Child_%i" % i)
        G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
        G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)
    draw_tree_nx(G, "test")

    # G.add_node(1, color='red', style='filled', fillcolor='blue', shape='square')
    # G.add_node(2, color='blue', style='filled')
    # G.add_edge(1, 2, color='green')
    # G.node[2]['shape'] = 'circle'
    # G.node[2]['fillcolor'] = 'red'