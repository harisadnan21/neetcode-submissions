class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromleft = [0 for i in range(len(nums))]
        fromright = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            if i == 0 :
                fromleft[i] = nums[i]
            else:
                fromleft[i] = fromleft[i -1] * nums[i]
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                fromright[i] = nums[i]
            else:
                fromright[i] = fromright[i + 1] * nums[i]

        print(fromleft)
        print(fromright)

        retarray = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                retarray[i] = fromright[1]
            elif i == len(nums ) -1:
                retarray[i] = fromleft[i -1]
            else:
                retarray[i] = fromleft[i -1] * fromright[i + 1]
        return retarray
        


