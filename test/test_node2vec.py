from unittest import TestCase
import networkx as nx

import matplotlib.pyplot as plt

class TestGraph(TestCase):
   # G = nx.MultiDiGraph()
    G = nx.Graph()
    G.add_edge('a', 'b', weight=0.6)
    G.add_edge('a', 'c', weight=0.2)
    G.add_edge('d', 'e', weight=0.1)
    G.add_edge('c', 'e', weight=0.7)
    G.add_edge('c', 'f', weight=0.9)
    G.add_edge('a', 'd', weight=0.6)
    G.add_edge('a', 'g', weight=0.7)
    G.add_edge('g', 'd', weight=0.6)
    G.add_edge('f', 'h', weight=0.7)
    G.add_edge('a', 'g', weight=0.6)
    G.add_edge('g', 'd', weight=0.8)
    G.add_edge('f', 'h', weight=0.9)
    G.add_edge('i', 'f', weight=0.6)
    G.add_edge('i', 'h', weight=0.9)
    G.add_edge('i', 'h', weight=0.6)
    G.add_edge('j', 'g', weight=0.8)
    G.add_edge('j', 'b', weight=0.7)
    G.add_edge('j', 'b', weight=0.6)

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge,
                           width=6)
    nx.draw_networkx_edges(G, pos, edgelist=esmall,
                           width=6, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()

    def test1(self):
        self.assertTrue(True)

    #def test_alias_setup(self):
     #   prob = [0.3, 0.4, 0.2, 0.1]
      #  my_graph = node2vec.Graph(TestGraph.G, False, 1, 1)
       # self.assertEquals(4, my_graph.alias_setup(prob))



if __name__ == '__main__':
    unittest.main()




