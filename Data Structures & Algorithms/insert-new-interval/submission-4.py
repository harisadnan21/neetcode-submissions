class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lst = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #put at the front 
                lst.append(newInterval)
                return lst + intervals[i:]
            elif newInterval[0] >intervals[i][1]:
                lst.append(intervals[i])
            else:
                
                newInterval= [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]
        lst.append(newInterval)
        return lst

            
        