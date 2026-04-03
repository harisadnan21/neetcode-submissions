class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sort
        #smash first two 
        # resort
        # continue until 1 left
        # max heap

        stones = [-1 * elem for elem in stones]
        heapq.heapify(stones)
        lenheap = len(stones)
        while lenheap > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            lenheap -= 2
            if x != y :
                heapq.heappush(stones, -1 * (abs(x) - abs(y)))
                lenheap +=1 
        
        return 0 if not stones else abs(stones[0])





        
        