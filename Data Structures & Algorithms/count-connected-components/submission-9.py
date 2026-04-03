class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = {i : [] for i in range(n)}
        count = 0
        print(graph)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        print(graph)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for elem in graph[node]:
                dfs(elem)
            return 
        for i in graph.keys():
            if i not in visited:
                count += 1
                dfs(i)
        return count

        