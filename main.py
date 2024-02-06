from graph_util import generate_random_graph, draw_graph_to_file, show_solution
from kruskal import kruskal
import re


# Generation parameters
n = 10
p = 0.25
max_weight = 10

# Generating and drwaing the graph
G = generate_random_graph(n, p , max_weight)
draw_graph_to_file(G, "graph.png")

# Finding the minimum spanning tree for the graph
mst = kruskal(n, G.edges(data = True))

# User input loop
print("""
Minimum Spanning Tree Game

Your goal is to find the correct minimum spanning tree for
the graph. Take a look at "graph.png" and start solving!

Here are the possible commands you can use:
    add (u,v)
    remove (u,v)
    submit
    help
    show
    exit
""")

def match_edge(edge):
    pattern = r"\((\d+),(\d+)\)"
    match = re.match(pattern, edge)
    if not match:
        return None

    u, v = map(int, match.groups())
    if u > v:
        u, v = v, u
    return u, v


selected_edges = set()

while True:
    user_input = input("Enter a valid command: ")
    user_input_list = user_input.strip().split(" ")

    match user_input_list:
        case ["add", edge]:
            nodes = match_edge(edge)
            if not nodes:
                print("Edge is not specificed with the correct format.\n")
                continue
            u, v = nodes

            if (u, v) not in G.edges:
                print("Cannot add edge that does not exist.\n")
                continue

            for edge in G.edges(data = True):
                if edge[0:-1] == (u, v):
                    w = edge[-1]["weight"]

            selected_edges.add((u, v, w))
            G.edges[u, v]["color"] = "red"
            draw_graph_to_file(G, "graph.png")
            print(f"Added the edge ({u},{v}).\n")

        case ["remove", edge]:
            nodes = match_edge(edge)
            if not nodes:
                print("Edge is not specificed with the correct format.\n")
                continue
            u, v = nodes

            if (u, v) not in G.edges:
                print("Cannot remove edge that does not exist.\n")
                continue

            for edge in G.edges(data = True):
                if edge[0:-1] == (u, v):
                    w = edge[-1]["weight"]

            if (u, v, w) not in selected_edges:
                print("Cannot remove an edge that was not selected.\n")
                continue

            selected_edges.remove((u, v, w))
            G.edges[u, v]["color"] = "black"
            draw_graph_to_file(G, "graph.png")
            print(f"Removed the edge ({u},{v}).\n")

        case ["submit"]:
            # TODO: implement submit
            pass

        case ["help"]:
            print("""
Here are the possible commands you can use with examples:

    add (u,v) : Adds the edge from u to v to your solution.
        `add (1,2)` adds the edge from node 1 to node
        2 to your solution.

    remove (u,v) : Removes the edge from u to v from your
        solution. `remove (1,2)` removes the edge from node
        1 to node 2 from your solution.

    submit : Submits your solution and checks if it is
        correct. In either case, it draws and prints the
        minimum spanning tree.

    help : Provides more detail about the valid commands.

    show : Draws and prints the minimum spanning tree.

    exit : Exits out of the program.
""")

        case ["show"]:
           show_solution(G, mst)
           break

        case ["exit"]:
            break

        case _:
            print("Invalid command. Type `help` to see some examples.\n")
