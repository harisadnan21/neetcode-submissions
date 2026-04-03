class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        currMax = 0
        for i, a in enumerate(nums):
            if i == 0:
                currMax = a

            elif i == 1:

                max1 = currMax
                currMax = max(nums[0], a)
            else:
                max2 = max1
                max1 = currMax
                currMax = max(a + max2, max1)
        return currMax
                

            
        