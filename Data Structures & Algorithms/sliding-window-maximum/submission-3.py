import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        ret = []
        for i in range(k):
            heapq.heappush(q,(-nums[i], i))
        ret.append(-q[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(q, ( -nums[i], i))
            while q[0][1] < i - k + 1:
                heapq.heappop(q)
            ret.append(-q[0][0])
        return ret        
