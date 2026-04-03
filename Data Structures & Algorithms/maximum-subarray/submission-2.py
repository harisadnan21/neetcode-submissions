class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestsum = float('-inf')
        currentsum = float('-inf')
        firstp = 0
        for i,a in enumerate(nums):
            currentsum += a
            if currentsum < a:
                #start from i 
                firstp = i
                #update sum and check
                currentsum = a

    
                
            if currentsum > largestsum:
                largestsum = currentsum
        return largestsum
                





        