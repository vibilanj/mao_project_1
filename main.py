import networkx as nx
import matplotlib.pyplot as plt
import random
from kruskal import kruskal, print_mst

random.seed(1) # TODO: remove seed

# Generation parameters
n = 10
p = 0.25
# TODO: add more parameters for weight ranges, node color, edge color, etc.

# Generating random connected graphs
G = nx.gnp_random_graph(n, p, seed = 1) # TODO: remove seed
while not nx.is_connected(G):
    G = nx.gnp_random_graph(n, p)

# Adding random weights to the edges
for (u, v) in G.edges():
    G.edges[u, v]["weight"] = random.randint(1, 10)
    G.edges[u, v]["color"] = "black"

def draw_graph_to_file(filename):
    pos = nx.circular_layout(G)
    color = [G.edges[u, v]["color"] for (u, v) in G.edges()]
    nx.draw(G, with_labels = True, pos = pos, edge_color = color)
    
    for i, e in enumerate(G.edges(data = True)):
        nx.draw_networkx_edge_labels(G, pos,
                                     edge_labels = {(e[0], e[1]): e[2]["weight"]},
                                     font_color = color[i])
        
    plt.savefig(filename)

# Drawing the question graph
draw_graph_to_file("graph.png")

# Finding the minimum spanning tree for the graph
mst = kruskal(n, G.edges(data = True))
# nx.write_edgelist(G, "graph.edgelist")
print_mst(mst)

# Drawing the solution graph
for (u, v, w) in mst:
    G.edges[u, v]["color"] = "red"
draw_graph_to_file("graph_mst.png")