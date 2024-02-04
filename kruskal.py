from disjoint_set import DisjointSet


#  Kruskal's algorithm for finding the minimum spanning tree of a graph.
def kruskal(n, edges):
    # Stores the resulting minimum spanning tree.
    mst = []
    # Index for sorted edges
    i = 0
    # Index for MST edges
    e = 0

    # Edges sorted by weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2]["weight"])

    # Disjoint set to check for cycles
    ds = DisjointSet(n)

    # The minimum spanning tree has n - 1 edges. This loops until the MST is 
    # completed.
    while e < n - 1:
        # Get the edge with the smallest weight.
        u, v, data = sorted_edges[i]
        w = data["weight"]
        i += 1

        u_rep = ds.find(u)
        v_rep = ds.find(v)

        # If adding the edge (u, v) to the MST does not form a cycle, add it
        # to the MST. Otherwise, discard it.
        if u_rep != v_rep:
            e += 1
            mst.append((u, v, w))
            ds.union(u_rep, v_rep)
    
    return mst


# Prints the cost and edges of the minimum spanning tree.
def print_mst(mst):
    minimum_cost = sum(w for (_, _, w) in mst)
    print(f"Minimum cost: {minimum_cost}")
    print("Edges: ")
    for u, v, w in mst:
        print(f"\t({u}, {v}): {w}")
