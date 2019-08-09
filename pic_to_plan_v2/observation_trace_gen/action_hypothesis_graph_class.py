import networkx as nx
import matplotlib.pyplot as plt
import random

class ActionGraph:

    def __init__(self):
        self.G = nx.DiGraph()
        self.G.add_node(0)
        self.node_nos = 0
        self.deepest_layer_nodes = [0]
        self.hierarchical = True



    def update(self, new_edges):
        new_deepest_layer_nodes = []
        n_e = []
        for d_l_n in self.deepest_layer_nodes:
            for x in new_edges:
                added_node_number = str(self.node_nos)+"_"+x[1]
                n_e.append((d_l_n, added_node_number))
                self.node_nos += 1
                new_deepest_layer_nodes.append(added_node_number)

        self.deepest_layer_nodes = new_deepest_layer_nodes
        self.G.add_edges_from(n_e)
        if(self.hierarchical):
            pos = self.hierarchy_pos(self.G, 0)
            nx.draw(self.G, pos=pos, with_labels=False)
            # rotate text labels
            text = nx.draw_networkx_labels(self.G, pos)
            for _, t in text.items():
                t.set_rotation("30")
        else:
            nx.draw(self.G, with_labels=True)
            pass

        #plt.savefig("path_graph_cities.png")
        #plt.show()

    def hierarchy_pos(self, G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

        '''
        From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
        Licensed under Creative Commons Attribution-Share Alike

        If the graph is a tree this will return the positions to plot this in a
        hierarchical layout.

        G: the graph (must be a tree)

        root: the root node of current branch
        - if the tree is directed and this is not given,
          the root will be found and used
        - if the tree is directed and this is given, then
          the positions will be just for the descendants of this node.
        - if the tree is undirected and not given,
          then a random choice will be used.

        width: horizontal space allocated for this branch - avoids overlap with other branches

        vert_gap: gap between levels of hierarchy

        vert_loc: vertical location of root

        xcenter: horizontal location of root
        '''
        if not nx.is_tree(G):
            raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

        if root is None:
            if isinstance(G, nx.DiGraph):
                root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
            else:
                root = random.choice(list(G.nodes))

        def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
            '''
            see hierarchy_pos docstring for most arguments

            pos: a dict saying where all nodes go if they have been assigned
            parent: parent of this branch. - only affects it if non-directed

            '''

            if pos is None:
                pos = {root:(xcenter,vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)
            if len(children)!=0:
                dx = width/len(children)
                nextx = xcenter - width/2 - dx/2
                for child in children:
                    nextx += dx
                    pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap,
                                        vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                        pos=pos, parent = root)
            return pos


        return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
