class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, a in enumerate(points):
            dist = pow(pow(a[0],2) + pow(a[1],2), 0.5)
            lst = [-dist, a]
            print(lst)
            if len(heap) < k:
                heapq.heappush(heap, lst)
            elif abs(lst[0]) < abs(heap[0][0]) :
                #insert and then pop
                heapq.heappush(heap,lst)
                heapq.heappop(heap)
            print(heap)
        retlst = [elem[1] for elem in heap]
        retlst = retlst[:: -1]
        return retlst
    
                



        