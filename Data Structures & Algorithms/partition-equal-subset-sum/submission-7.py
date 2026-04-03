class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        half = sum(nums) / 2

        dp = set()
        dp.add(0)
        for i in range(len(nums) -1, -1, -1):
            newSet = set()
            for elem in dp:
                newelem = elem + nums[i]
                if newelem == half:
                    return True
                newSet.add(newelem)
                newSet.add(elem)
            dp = newSet
        return False



        