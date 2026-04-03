class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[heights[row][col] for col in range(len(heights[0]))] for row in range(len(heights))]
        atlantic = [[heights[row][col] for col in range(len(heights[0]))] for row in range(len(heights))]
        
        def dfs(row, col, num_before, grid):
            #does dfs
            if row < 0 or col < 0 or row > len(heights) -1 or col > len(heights[0]) -1 or grid[row][col] == -1 or grid[row][col] < num_before:
                return
            else:
                num = grid[row][col]
                grid[row][col] = -1
                dfs(row + 1, col, num, grid)
                dfs(row -1, col, num, grid)
                dfs(row, col + 1, num, grid)
                dfs(row, col -1, num, grid)



        for row in range(len(heights)):
            for col in range(len(heights[0])):
                #do dfs on top left
                if row == 0 or col == 0:
                    dfs(row, col, pacific[row][col], pacific)
            
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                # do dfs on bottom right
                if row== len(heights) -1 or col ==len(heights[0]) -1:
                    dfs(row , col, atlantic[row][col ], atlantic)
        ret = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if pacific[row][col] == -1 and atlantic[row][col] == -1:
                    ret.append([row, col])
        return ret
                
        

                
        