class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retlst = []
        currSubSet = []

        def backtrack(index):
            if index >= len(nums):
                ## backtracking has reached base chase
                addingSet = currSubSet.copy()
                retlst.append(addingSet)
                return

            currSubSet.append(nums[index])
            backtrack(index + 1)

            currSubSet.pop()
            backtrack(index + 1)
        backtrack(0)
        return retlst
