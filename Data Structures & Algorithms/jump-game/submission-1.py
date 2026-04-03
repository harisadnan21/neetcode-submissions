class Solution:
    def canJump(self, nums: List[int]) -> bool:
        minReachedIdx = len(nums)-1
        for i in range(len(nums)-2, - 1, -1):
            if minReachedIdx - i <= nums[i]:
                minReachedIdx = i

        

        return minReachedIdx ==0
   
        