class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for row in range(len(text1))] for col in range(len(text2))]

        for row in range(len(grid) -1 , -1, -1):
            for col in range(len(grid[0]) -1, -1, - 1):
                if text1[col] == text2[row]:
                    grid[row][col] = 1 +(grid[row + 1][col + 1] if (col< len(grid[0]) - 1 and row < len(grid) - 1) else 0) 
                else:
                    grid[row][col] = max((grid[row][col + 1] if col< len(grid[0]) -1 else 0),(grid[row+ 1][col] if row < len(grid) -1 else 0 ))
                    

        return grid[0][0]


        