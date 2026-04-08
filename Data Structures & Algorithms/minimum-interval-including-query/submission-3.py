class Solution:
    import heapq
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQueries = sorted(queries)
        # query : len
        res = {}

        minheap = []
        # first add all intervals to the min heap with start time <= q. keep idx,
        # add the [length, endtime]
        intervals_idx =0
        for q in sortedQueries:
            while (intervals_idx < len(intervals) and intervals[intervals_idx][0] <= q):
                r = intervals[intervals_idx][1]
                l = intervals[intervals_idx][0]
                heapq.heappush(minheap , [r - l + 1, r])
                intervals_idx += 1

        # then as we pop we must not consider the elems that are invalid ( end time < q),
        # first valid one is what we return
            while len(minheap) > 0 and minheap[0][1] < q:
                #pop
                heapq.heappop(minheap)
            if len(minheap) == 0:
                res[q] = -1
            else:
                res[q] = minheap[0][0]
    
        return [res[q] for q in queries]
