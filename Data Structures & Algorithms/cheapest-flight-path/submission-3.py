class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Use Bellman ford to find hte path for least price src -> dst, 
     # since bellman ford is essentially n - 1 times for loop for relaxations 
     # for all nodes , it is done in sequential order
        # if no edge from src to dst: return -1, do this using BFS
        dist = [float("inf")] * n
        dist[src] = 0
        for layer in range(k + 1):
            tmpDist = dist[:]
            for u, v, d in flights:
                if tmpDist[u] == float("inf"):
                    continue
                if dist[u] + d < tmpDist[v]:
                    tmpDist[v] = dist[u] + d
            dist = tmpDist



        return -1 if dist[dst] == float("inf") else dist[dst]
        
        


