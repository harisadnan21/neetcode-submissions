class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def countIslands(row, col ):
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) -1 or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                countIslands(row +1, col)
                countIslands(row -1, col)
                countIslands(row, col + 1)
                countIslands(row,col -1)
                return
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # countIsland returns 1 or 0.
                if grid[row][col] == "1":
                    count += 1
                    countIslands(row, col)
        return count