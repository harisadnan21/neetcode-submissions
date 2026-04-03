class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t)> len(s):
            return 0

        m = len(s)
        n = len(t)

        # create a dp 2d array with rows as elems of s, cols as elems of t
        dp = [[0 for col in range(0, n + 1)] for row in range(0, m +1)]
        for row in range(0,len(dp)):
            for col in range(0,len(dp[0])): 
                if col == 0:
                    dp[row][col] = 1


        dp[0][0] = 1
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                i = row -1
                j = col - 1

                if row ==0 or col == 0 or j > i :
                    continue
                if s[i] == t[j]:
                    dp[row][col] = dp[row -1][col -1] + dp[row -1][col]
                else:
                    dp[row][col] = dp[row -1][col]

        return dp[m][n]