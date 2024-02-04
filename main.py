import networkx as nx
import matplotlib.pyplot as plt

# Generating random connected graphs
p = 0.4
G = nx.gnp_random_graph(10, p)
while not nx.is_connected(G):
    G = nx.gnp_random_graph(10, p)

nx.draw(G)
plt.savefig("graph.png")