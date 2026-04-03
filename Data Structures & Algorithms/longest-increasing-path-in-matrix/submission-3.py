class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # (r, c) : LIP
        dp = {}
        def dfs(r, c, prevVal):
            if r< 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] <= prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            ret = 0
            ret = max(ret, 1 + dfs(r + 1, c, matrix[r][c]))
            ret = max(ret, 1 + dfs(r - 1, c, matrix[r][c]))
            ret = max(ret, 1 + dfs(r, c + 1, matrix[r][c]))
            ret = max(ret,1 +  dfs(r, c -1, matrix[r][c]))
            dp[(r, c)] = ret
            print(dp)
            return ret
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dfs(row, col, -1)
                
        return max(dp.values())


        
        