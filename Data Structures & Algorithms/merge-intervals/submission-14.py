class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        curr = 0
        
        lst = []
        intervals.sort()
        currElem = intervals[0]
        print(intervals)
        if len(intervals) == 1:
            return intervals
        j = 1
        #len(intervals) > 2

        while j <= len(intervals) -1:
            print(curr, j)
            print(currElem)
            #append curr to lst when not intersection, then j = curr
            # when intersection,reevaluate curr and j ++
            if currElem[1] >= intervals[j][0]:
                currElem = [currElem[0], max(currElem[1], intervals[j][1])]
                j = j + 1

            else:
                lst.append(currElem)
                curr = j
                j +=1 
                currElem = intervals[curr]

        lst.append(currElem)
        return lst



        