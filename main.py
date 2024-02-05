from graph_util import generate_random_graph, draw_graph_to_file, show_solution
from kruskal import kruskal

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

while True:
    user_input = input("Enter a valid command: ")
    user_input_list = user_input.strip().split(" ")

    match user_input_list:
        case ["add", edge]:
            print("add")

        case ["remove", edge]:
            print("remove")

        case ["submit"]:
            print("submit")

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
