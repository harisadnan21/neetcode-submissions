class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
            # Build adjacency list
        g = defaultdict(list)
        for a, b in tickets:
            g[a].append(b)
            if b not in g:
                g[b] = g[b]  # ensure key exists (no-op but keeps defaultdict keys visible)

        # Sort neighbors so we try lexicographically smallest first
        for u in g:
            g[u].sort()

        path = []
        def dfs(u):
            # consume edges one by one in sorted order
            while g[u]:
                v = g[u].pop(0)   # pop the smallest neighbor (O(deg), fine for small inputs)
                dfs(v)
            path.append(u)

        dfs("JFK")
        return path[::-1]