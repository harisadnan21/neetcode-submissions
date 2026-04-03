class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1 for _ in range(amount + 1)]

        def recurse(currsum):
            if currsum < 0:
                return float('inf')
            if currsum == 0:
                return 0
            if dp[currsum] != -1:
                return dp[currsum]

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + recurse(currsum - coin))

            dp[currsum] = best
            return best

        ans = recurse(amount)
        return -1 if ans == float('inf') else ans