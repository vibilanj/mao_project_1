from graph_util import generate_random_graph, draw_graph_to_file, n
from kruskal import kruskal, print_mst

# Generating and drwaing the graph
G = generate_random_graph()
draw_graph_to_file(G, "graph.png")

# Finding the minimum spanning tree for the graph
mst = kruskal(n, G.edges(data = True))
print_mst(mst)

# Drawing the solution graph
for (u, v, w) in mst:
    G.edges[u, v]["color"] = "red"
draw_graph_to_file(G, "graph_mst.png")