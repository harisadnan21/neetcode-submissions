class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # we keep a dp array of len(nums) but it will hold the max and min values for the 
        # subarrays formed till that index
        dp = [[0, 0] for elem in nums]

        for idx in range(len(nums)):
            if idx == 0:
                dp[idx]= [nums[idx], nums[idx]]
            
            else:
                dp[idx] = [max(nums[idx], dp[idx -1][0] * nums[idx], dp[idx -1][1] * nums[idx]),
                min(nums[idx], dp[idx -1][0] * nums[idx], dp[idx -1][1] * nums[idx])]
        
        ret = float("-inf")
        for elem in dp:
            if elem[0] > ret:
                ret = elem[0]
        return ret