class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i, a in enumerate(nums):
            heapq.heappush(heap, a)
            if len(heap) > k:
                #remove
                heapq.heappop(heap)
        return heap[0]
        