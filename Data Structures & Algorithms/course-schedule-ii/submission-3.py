class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [course, prereq]
        graph = { i: [] for i in range(numCourses)}

        #{1 : [2,3]
        #, ..}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        #DFS
        #courses taken in current path
        ret = []
        visiting = set()
        globalvisited = set()

        def dfs(currcourse):
            #return empty list if cycle found
            if currcourse in visiting:
                return False
            if currcourse in globalvisited:
                return True
            visiting.add(currcourse)
            
            for pre in graph[currcourse]:
                if not dfs(pre):
                    return False
                
            visiting.remove(currcourse)
            globalvisited.add(currcourse)
            ret.append(currcourse)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return ret
        