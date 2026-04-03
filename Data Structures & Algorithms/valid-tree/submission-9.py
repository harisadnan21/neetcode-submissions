class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # cycle detected
            parent[rootY] = rootX  # union
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True  # no cycles, and n - 1 edges guarantee connectivity