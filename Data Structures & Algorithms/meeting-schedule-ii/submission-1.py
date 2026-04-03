"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) ==1 :
            return 1
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s = 0
        e = 0
        maxcount = 0
        count= 0
        while s < len(start):
            if end[e] <= start[s]:
                count -= 1
                e +=1 
            else:
                count += 1
                s +=1 
                maxcount = max(maxcount, count)
            
        return maxcount
        
        