from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # is there a path that goes through all nodes without a cycle?
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True
            visited.add(node)
            for value in graph[node]:
                
                if not dfs(value):
                    return False
            visited.remove(node)
            graph[node] = []
            return True


        #create adj graph
        graph = defaultdict(list)
        for course in range(numCourses):
            graph[course]= []
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        print(graph)


        #DFS
        #do dfs on every node and keep on exporing till all the graph is explored
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



            