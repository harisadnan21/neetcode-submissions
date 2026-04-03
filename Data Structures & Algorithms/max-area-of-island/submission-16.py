class Solution:
    def __init__(self):
        self.maxval = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0 
            retval = 1 + dfs(i + 1, j) +dfs(i, j + 1) +dfs(i -1, j) + dfs(i, j -1)
            
            self.maxval = max(self.maxval,retval)
            return retval
        i = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                i +=1
                dfs(row, col)
        return self.maxval

        