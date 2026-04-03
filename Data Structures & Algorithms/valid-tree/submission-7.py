class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if len(edges) != n-1:
            return False

        def dfs(n, parent):
 
            #check for loops
            retval = True
            for child in graph[n]:
        
                if child == parent:
                    continue
                if child in visited:
                    return False
                visited.add(child)
                retval = retval and dfs(child, n)
            
            return retval
            
        visited = set()    
        visited.add(0)

        return dfs(0, -1) and len(visited) == n