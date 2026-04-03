class Solution:
    import heapq 
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # [0,0],[2,2],[3,3],[2,4],[4,2]
        
        # maintain a min heap and a visited set
        visited = set()
        minheap= []
        edges = {}
        if len(points) == 1:
            return 0
        for idx1, point1 in enumerate(points):
            for idx2, point2 in enumerate(points):
                if idx1 != idx2:
                    x1, y1 = point1[0], point1[1]
                    x2, y2 = point2[0], point2[1]

                    dist = abs(x1 -x2) + abs(y1 - y2)
                    if (x1, y1) not in edges:
                        edges[(x1, y1)] = []
                    edges[(x1, y1)].append([dist, x2, y2])
        
        heapq.heappush(minheap, [0,points[0][0], points[0][1]])
        cost = 0
        while len(visited) != len(points):
            closestEdge = heapq.heappop(minheap)
            if (closestEdge[1], closestEdge[2]) in visited:
                continue
            visited.add((closestEdge[1], closestEdge[2]))
            cost+= closestEdge[0]
            #add the neighbors with the weight to the minheap
            for neigh in edges[(closestEdge[1], closestEdge[2])]:
                heapq.heappush(minheap, [neigh[0], neigh[1], neigh[2]])    
        

        return cost
