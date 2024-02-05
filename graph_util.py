import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(1) # TODO: remove seed


# Generate a random connected weighted graph.
def generate_random_graph(n, p, max_weight):
    # Generating random connected graphs
    G = nx.gnp_random_graph(n, p, seed = 1) # TODO: remove seed
    while not nx.is_connected(G):
        G = nx.gnp_random_graph(n, p)

    # Adding random weights to the edges
    for (u, v) in G.edges():
        G.edges[u, v]["weight"] = random.randint(1, max_weight)
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


# Prints the cost and edges of the minimum spanning tree.
def print_mst(mst):
    minimum_cost = sum(w for (_, _, w) in mst)
    print(f"Minimum cost: {minimum_cost}")
    print("Edges: ")
    for u, v, w in mst:
        print(f"\t({u}, {v}): {w}")


# Drawing and printing the solution
def show_solution(G, mst):
    for (u, v, _) in mst:
        G.edges[u, v]["color"] = "red"
    draw_graph_to_file(G, "graph.png")
    print_mst(mst)

