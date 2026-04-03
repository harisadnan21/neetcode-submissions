class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # row = indexes, columns = boughtPrice
        dp = [[-1] * (max(prices) + 2) for _ in range(len(prices))]        # consider for boughtPrice beign -1

        def recurse(idx, boughtPrice):
            profit = 0
            if idx >= len(prices):
                return 0
            cache_idx = boughtPrice + 1
            if dp[idx][cache_idx] != -1:
                return dp[idx][cache_idx]
            if boughtPrice > -1:
                # you have a coin
                profit = max(prices[idx] -boughtPrice + recurse(idx + 2, -1), recurse(idx +1, boughtPrice))
            else:
                # you dont have a coin yet
                profit = max(recurse(idx + 1, prices[idx]), recurse(idx + 1, boughtPrice))
            dp[idx][cache_idx] = profit
            return profit
        return recurse(0, -1)


        # keep price brought 
        # at each index, if you have a coin, and curr price > price brought
        # you can either sell it or keep it
        # (buy, 0) , (sell, 1)
        

