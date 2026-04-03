class Solution:
    def __init__(self):
        self.maxval = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            q = []
            q.append([i, j])
            currval = 0
            while q:

                currIdx = q.pop(0)
                row = currIdx[0]
                col = currIdx[1]
                print(currIdx)
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] ==0:
                    #invalid index
                    continue
                
                #visit elem
                grid[row][col] = 0
                currval +=1
                q.append([row + 1, col])
                q.append([row -1, col])
                q.append([row, col + 1])
                q.append([row, col -1])
            return currval


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = bfs(row, col)
                self.maxval = max(self.maxval, val)

        return self.maxval
        




        