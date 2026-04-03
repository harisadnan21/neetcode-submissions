class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = {}
        def recurse(l, r):
            if l > r :
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):

                coins = nums[i] * nums[l -1] * nums[r + 1]
                coins += recurse(l, i -1) + recurse(i + 1, r)
                dp[(l, r)]= max(dp[(l, r)], coins)

            return dp[(l,r)]
                
        return recurse(1, len(nums) -2)

