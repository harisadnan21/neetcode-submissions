class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # each integer, you have option to include or not 
        # [1,2,1]
        # 1.         2           1
        # [1] -> [1], [1,2] -> [1], [1,1], [1,2],[1,2,1]
        # [] -> [],[2]      -> [], [1], [2],[2,1]
        # [1,1,2]
        # [1] -> [1],[1,1]
        # [] -> [], [1]
        res = []
        nums.sort()
        def backtrack(idx, subset):
            if idx == len(nums):
                res.append(subset)
                return
            
            ## add the val at the current index
            subset.append(nums[idx])
            backtrack(idx +1 , subset[:])
            subset.pop()

                # at last , idx = len(nums) -1
            # dont include the next repeated values
            while idx < len(nums) -1 and nums[idx]== nums[idx + 1]:

                idx +=1
            backtrack(idx + 1, subset[:])


        backtrack(0, [])

        return res
