class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[(float("inf")) for col in range(len(word2) + 1)] for row in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == len(word1):
                    dp[i][j] = len(word2) - j
                if j == len(word2):
                    dp[i][j] = len(word1) - i
        print(dp)
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2)- 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+ 1][j +1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j+ 1], dp[i][j + 1], dp[i + 1][j])


        return dp[0][0]