import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.currlen = 0
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)


        #max and min heap, keep each heap's size and decide for the odd and even case

    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0 or num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        self.currlen += 1
        if abs(len(self.minheap) - len(self.maxheap)) > 1 :
            self.rebalance()
        

        
    def rebalance(self) -> None:
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        else:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        
    def findMedian(self) -> float:
        if self.currlen % 2 == 0:
            lowerMax = -self.maxheap[0]
            upperMin = self.minheap[0]
            return (lowerMax + upperMin) / 2

        else:
            return -self.maxheap[0] if len(self.maxheap) > len(self.minheap) else self.minheap[0]

        
        