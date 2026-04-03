class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #at each index,  option of including or not
        ret = []

        def backtrack(index, currLst, currSum):
    
            if currSum == target:
                ret.append(currLst)
                return
            if index >= len(nums) or currSum > target:
                return
            
            # add elem, next one is same elem

            currLst.append(nums[index])
            currSum += nums[index]
            backtrack(index, currLst.copy(), currSum)
            #dont add elem

            currLst.pop()
            currSum -= nums[index]
            backtrack(index + 1, currLst.copy(),currSum)
            
        
        backtrack(0, [], 0)
        return ret


