class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if not intervals or len(intervals) == 1:
            return 0
        # remove the interval with the bigger end value if intersection occurs
        ret = 0
        last =0
        curr = 1
        while curr <= len(intervals) -1:
            currInterval = intervals[curr]
            lastInterval = intervals[last]
            if lastInterval[1] > currInterval[0]:
                #intersection occurs 
                if currInterval[1] < lastInterval[1]:
                    last = curr
                ret +=1
            else:
                last = curr
            curr +=1 
        return ret

        










































