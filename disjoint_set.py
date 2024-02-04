# Disjoint Set data structure for the Union-Find algorithm
# This is used to check whether the edge that we are considering adding to the
# spanning tree forms a cycle or not.
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n


    # Finds the representative of the set that contains x.
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    # Unions the sets that contain x and y.
    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep == y_rep:
            return
        
        if self.rank[x_rep] < self.rank[y_rep]:
            self.parent[x_rep] = y_rep
        elif self.rank[x_rep] > self.rank[y_rep]:
            self.parent[y_rep] = x_rep
        else:
            self.parent[y_rep] = x_rep
            self.rank[x_rep] += 1
