from graph_util import *
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

# Instructions for usage
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

# Matches the edges in (u,v) format and returns the nodes (smallest first).
def match_edge(edge):
    pattern = r"\((\d+),(\d+)\)"
    match = re.match(pattern, edge)
    if not match:
        return None

    u, v = map(int, match.groups())
    if u > v:
        u, v = v, u
    return u, v

# Set to store edges selected by the user.
selected_edges = set()

# User input loop
while True:
    user_input = input("Enter a valid command: ")
    user_input_list = user_input.strip().split(" ")

    match user_input_list:
        # Add an edge to the selection
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

        # Remove an edge from the selection
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

        # Submit the selection and check if it is a valid minimum spannign tree.
        case ["submit"]:
            if len(selected_edges) != len(mst):
                print("Incomplete solution.\n")
                continue

            minimum_cost = sum(w for (_, _, w) in mst)
            selected_cost = sum(w for (_, _, w) in selected_edges)

            if minimum_cost != selected_cost:
                print("Wrong solution.\n")
                continue

            print("Correct solution! Here the generated minimum spanning tree:\n")
            print_mst(mst)
            break

        # Provide more information about program usage.
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

        # Show the generated minimum spanning tree solution.
        case ["show"]:
           show_solution(G, mst)
           break

        # Exit the program.
        case ["exit"]:
            break

        # Catch invalid commands.
        case _:
            print("Invalid command. Type `help` to see some examples.\n")
