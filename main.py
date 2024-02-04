import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(1) #TODO: remove later

# Generating random connected graphs
p = 0.25
G = nx.gnp_random_graph(10, p, seed=1) #TODO: remove seed
while not nx.is_connected(G):
    G = nx.gnp_random_graph(10, p)

for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 10)

# print(G.edges(data=True))

pos = nx.circular_layout(G)
nx.draw(G, with_labels=True, pos=pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.savefig("graph.png")

nx.write_edgelist(G, "graph.edgelist")