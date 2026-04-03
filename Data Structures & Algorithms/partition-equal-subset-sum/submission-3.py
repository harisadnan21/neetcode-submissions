class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        half = sum(nums) / 2

        def helper(currIdx, visitedSet, rem):
            if currIdx in visitedSet:
                return False
            visitedSet.add(currIdx)
            rem -= nums[currIdx]

            if rem == 0:
                return True
            elif rem < 0:
                return False
            else:
                for i in range(len(nums)):
                    if helper(i, visitedSet.copy(), rem):
                        return True
                return False
                
        for i in range(len(nums)):
            if helper(i, set(), half):
                return True
        return False



        