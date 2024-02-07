# Modelling and Optimization Project 1

## Introduction

This project is an interactive game that allows users to practice their understanding of minimum spanning trees (MST). When you run the program, it generates a random weighted graph and saves it to a file. The user can view the file and interact with the program through the command line to select edges. When they are satisfied with their selection, they can submit it and receive feedback from the program.

## Implementation Details

The project is implemented in Python. Among the two possible implementations I proposed, I opted for the command line-based interface (CLI) as it was easier to implement but had most of the advantages of the graphical user interface. The CLI provided a reasonable level of interactivity as the graph image was updated with each command. Additionally, the user can see their selected edges in a different color and when they submit their selection, the solution is both printed to the console and displayed in the image.

Here are the descriptions of the four Python files. Furthermore, the code in each file is documented with comments to explain each part in greater detail.

### `disjoint_set.py`

This file contains the implementation of a disjoint set data structure for the union-find algorithm. The disjoint set comes in handly for our minimum spanning tree algorithm as it allows us to efficiently check whether the edge that we are considering adding to the minimum spanning tree forms a cycle or not.

### `kruskal.py`

This file contains the main algorithm of the project: Kruskal's algorithm for finding the minimum spanning tree of a graph. Briefly here are the steps taken by the algorithm:

1. Sort the edges of the graph by their weights in ascending order.
2. For each edge, we check that adding the edge does not create a cycle.
3. If it does not form a cycle, we can add it to our minimum spanning tree. If it does, we discard it.

### `graph_util.py`

This file contains some helpful utility functions for the graphs:

-  `generate_random_graph` creates a random connected graph with given generation parameters and populates each edge with a random weight.

- `draw_graph_to_file` takes a graph, creates an image with its nodes, edges and weights and saves it to a given filename.

- `print_mst` takes in the minimum spanning tree of the graph and prints its total edge weight (minimum cost) and the edges that make up the minimum spanning tree.

- `show_solution` updates the graph with the minimum spanning tree solution, updates the image and prints the minimum spanning tree information.

### `main.py`

This file is the main runner file. The generation parameters of the random graphs are defined here:

- $n$ determines the number of nodes in the graph (default is 10).
- $p$ determines the probability of edge creation between nodes (default is 0.25).
- `max_weight` determines the maximum weight of the edges. Edge weights are randomly chosen from 1 to `max_weight`.

With these parameters, the random connected weighted graph is generated and saved to a file (default is `graph.png`). Then, the minimum spanning tree for this graph is calculated using Kruskal's algorithm. A helpful function `match_edge` is defined to match the edges from user input and return it in the correct format. We also initialize a set to store the edges selected by the user.

We can now begin the game by printing out the introduction message to the console. This explains the basic syntax of interacting with the program. Then, we begin the input loop. This loop runs indefinitely, capturing the user input and processing it accordingly. The valid commands and their effects are as follows:

### `add`
Allows the user to add an edge to their selection. The users are notified if they fail to specify it the edge in the correct format or if they attempt to select an edge that is not in the graph. If the edge is valid, then it is added to their selection and the graph is updated with the edge colored in red.

### `remove`
Allows the user to remove an edge from their selection. Similar to `add` the user is notified if they fail to specify the edge in the correct format or if they try to remove an edge that does not exist. Additionally, they will also be notified if they try to remove an edge that they never selected. If the edge is valid, then it is removed from their selection and the graph by reverting the color of the removed edge to black.

### `submit`
Allows the user to submit their selection of edges as the minimum spanning tree. First, a sanity check is conducted. For a graph of $n$ nodes the minimum spanning tree must contain $n - 1$ edges. If the number of selected edges is less than this, they are notified that their solution is incomplete and the program continues.

If they have the correct number of edges in their selection, then the solution is properly checked. To ensure that their answer is correct, we can either:

1. check that the selected edges are the same as the minimum spanning tree calculated by the program. This only works for graphs that have a unique minimum spanning tree. Minimum spanning trees are guaranteed to be unique when each edge has a distinct weight (see https://en.wikipedia.org/wiki/Minimum_spanning_tree#Uniqueness), or
2. check that the total edge weights (minimum cost) is the same for both the user-selected minimum spanning tree and the minimum spanning tree calculated by the program. This works regardless of uniqueness.

Since we cannot reason about the uniqueness of the randomly generated graphs (edge weights can be duplicated), the user's solution is checked by comparing the total edge weights.

### `help`
Provides more detailed information about the commands understood by the programs (including examples).

### `show`
Shows the minimum spanning tree solution generated by the program.

### `exit` and default case
Exits the program safely. There is also a default case that catches invalid commands and prompts the user to check out the help message.

## Further Improvements

As previously mentioned, an improvement to this project could be the implementation of a graphical user interface that makes it easier for the user to interact with the program. Additionally, the graph generation parameters could be exposed to the user, allowing them greater customization of the difficulty of the game.

From a purely technical standpoint, there are no assumptions made in this project and the algorithm is guaranteed to work every time, even with much larger graphs. However, the program would definitely start to slow down with large graphs and the graph visualizer might not be very clear when there are many nodes and edges.

## How to Run

### Setting up the enviroment

1. Ensure that you have a working install of Python 3.11.6.
2. Navigate to the directory containing the project in your terminal.
3. Create a Python virtual environment by running `python3 -m venv .venv`.
4. Use the virtual environment with `source .venv/bin/activate`.
5. Install the necessary packages using `pip install -r requirements.txt`.

### Running the program

1. Navigate to the project directory.
2. Make sure that the virtual environment is activated. If it is not, use `source .venv/bin/activate`.
3. Run the program with `python main.py`.
4. Open the image `graph.png` (preferably in a program that refreshes the image when it changes)
5. Interact with the program by typing your commands into the terminal window.