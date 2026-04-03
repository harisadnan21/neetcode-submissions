from collections import Counter, deque

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = 0
        
        dic = Counter(tasks)
        q = deque()
        heap = []
        for key in dic:
            heapq.heappush(heap, [-dic[key], key])

        while count != len(tasks):
            while q and time - q[0][1] > n:
                elem = q.popleft()[0]
                print("q:", elem)
                if dic[elem] > 0:

                    heapq.heappush(heap, [-dic[elem], elem])

            if heap: 
                maxchar = heapq.heappop(heap)[1]
                dic[maxchar] -=1
                q.append([maxchar, time])
                count += 1

            time += 1
        return time

        