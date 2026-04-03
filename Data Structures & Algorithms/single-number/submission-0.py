class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # double pointer, window, iterate from either side
        res = 0 
        for num in nums:
            res ^= num

        return res

        