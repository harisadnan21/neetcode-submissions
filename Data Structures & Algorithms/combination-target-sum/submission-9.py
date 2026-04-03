class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #[2,5,6,9] , 9
        retlst = []
        currelems = []

        def backtrack(index, currsum):
            if index >= len(nums) or currsum > target:
                #invalid case
                return

            if currsum == target:
                # correct combination
                retlst.append(currelems.copy())
                return
            
            #incomplete combination
            
            # include index elem
            currsum += nums[index]
            currelems.append(nums[index])
            backtrack(index, currsum)

            # not including index elem
            currsum -= nums[index]
            currelems.pop()
            backtrack(index +1, currsum)
            return

        backtrack(0, 0)

        return retlst

