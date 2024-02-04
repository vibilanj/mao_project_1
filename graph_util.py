import networkx as nx
import matplotlib.pyplot as plt
import random

# Generation parameters
n = 10
p = 0.25
# TODO: add more parameters for weight ranges, node color, edge color, etc.

random.seed(1) # TODO: remove seed


# Generate a random connected weighted graph.
def generate_random_graph():
    # Generating random connected graphs
    G = nx.gnp_random_graph(n, p, seed = 1) # TODO: remove seed
    while not nx.is_connected(G):
        G = nx.gnp_random_graph(n, p)

    # Adding random weights to the edges
    for (u, v) in G.edges():
        G.edges[u, v]["weight"] = random.randint(1, 10)
        G.edges[u, v]["color"] = "black"

    return G


# Draw the graph to a file.
def draw_graph_to_file(G, filename):
    pos = nx.circular_layout(G)
    color = [G.edges[u, v]["color"] for (u, v) in G.edges()]
    nx.draw(
        G,
        with_labels = True,
        pos = pos,
        edge_color = color,
        font_color = "white",
        font_weight = "bold",
        font_size = 10
    )
    
    for i, e in enumerate(G.edges(data = True)):
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels = {(e[0], e[1]): e[2]["weight"]},
            font_color = color[i]
        )
        
    plt.savefig(filename)
