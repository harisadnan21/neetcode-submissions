class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sumactual = (n * (n + 1))//2 
        sumfound = sum(nums)     
        return sumactual - sumfound