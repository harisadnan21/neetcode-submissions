import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find the path from (0,0) to [n-1, n- 1]nwith the smallest maximum value
        #use dijkstra's algo

        #1.Create graph

        graph = {}
        # {(i, j) : [(i1, j1), (i2, j2)]}

        costs = {}
        #{(i, j) : dist}
        
        heap= [[grid[0][0], (0,0)]]
        # [[0, (i, j)]]

        #create graph
        for row in range(len(grid)):
            for col in range(len(grid)):
                graph[(row, col)] = []
                costs[(row,col)] = float("inf")
                if row > 0 : 
                    graph[(row, col)].append((row - 1, col ))
                if row  < len(grid ) - 1:
                    graph[(row, col)].append((row+ 1, col))
                if col > 0:
                    graph[(row, col)].append((row, col -1))
                if col < len(grid)-1: 
                    graph[(row, col)].append((row , col +1))

        print(graph)
        costs[(0, 0)] = grid[0][0]
        while heap:
            currCost , currNode = heapq.heappop(heap)
            if costs[currNode] < currCost:
                continue
            
            #we want to keep going on this path
            for neigh in graph[currNode]:
                newCost = max(grid[neigh[0]][neigh[1]], currCost)
                if newCost < costs[neigh]:
                    costs[neigh] = newCost
                    heapq.heappush(heap,[newCost, neigh])


        return costs[(len(grid)-1, len(grid)-1)]