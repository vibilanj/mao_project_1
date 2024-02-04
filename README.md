# Modelling and Optimization Project 1

## Proposal

**Interactive Minimum Spanning Tree Game**

The project proposes an interactive game focusing on minimum spanning tree (MST) algorithms to reinforce concepts discussed in our class. Users will be presented with a randomly generated weighted network, and tasked with constructing a minimum spanning  tree by strategically selecting edges. The program will validate user solutions to ensure that they are connected and have the minimum distance. If the user's solution is incorrect, the program could offer the correct MST edges.

The project offers flexibility in implementation, and there are two potential options for user interaction. In the first approach, the program outputs the randomly generated weighted graph to an image file, which the users can view. Users then interact with a command line interface to manually select edges, and upon completion, they signal the program to check their solution. The program verifies the user's solution and prints whether it is correct.

Alternatively, for a more interactive experience (time permitting), a graphical user interface (GUI) can be implemented using a library like "pygame". The randomly generated weighted graph is displayed on the GUI, and users can interact by clicking directly on edges to mark them in a different colour. A submit button allows users to signal completion, triggering the program to check the validity of their solution. In this scenario, the GUI not only enhances user engagement but also provides immediate visual feedback.

## Notes

- To ensure that the answer is correct, we can either check that the minimum cost is the same (regardless of uniqueness) or check that the edges provided for the MST are exactly the same (only works for graphs that have a unique minimum spanning tree)
- Minimum spanning trees are guaranteed to be unique when each edge has a distinct weight (see https://en.wikipedia.org/wiki/Minimum_spanning_tree#Uniqueness)
