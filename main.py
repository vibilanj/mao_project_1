from graph_util import generate_random_graph, draw_graph_to_file
from kruskal import kruskal, print_mst

# Generation parameters
n = 10
p = 0.25
max_weight = 10

# Generating and drwaing the graph
G = generate_random_graph(n, p , max_weight)
draw_graph_to_file(G, "graph.png")

# Finding the minimum spanning tree for the graph
mst = kruskal(n, G.edges(data = True))
print_mst(mst)

# Drawing the solution graph
for (u, v, w) in mst:
    G.edges[u, v]["color"] = "red"
draw_graph_to_file(G, "graph_mst.png")

# TODO: implement the main loop with the following commands
# add
# remove
# submit 
# show
# exit

# Input for add and remove can be as follows
# (u,v)
# u->v
# u,v
# u v