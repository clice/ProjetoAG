import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.G = nx.Graph()

    def add_node(self, node):
        self.G.add_node(node)

    def add_nodes(self, nodes):
        self.G.add_nodes_from(nodes)

    def add_edge(self, node1, node2):
        self.G.add_edge(node1, node2)

    def add_edges(self, edges):
        self.G.add_edges_from(edges)

    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()
