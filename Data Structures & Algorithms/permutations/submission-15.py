class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []


        def backtrack(currIndex, lstLeft, lstConst):
            print(currIndex, lstLeft, lstConst)
            if currIndex >= len(nums):
                # you've iterated all the way through
                ret.append(lstConst.copy())
                return
            
            for i, a in enumerate(lstLeft):
                
                backtrack(currIndex + 1, lstLeft[: i] + lstLeft[i + 1:] , lstConst.copy() + [a])

            return

        backtrack(0, nums.copy(), [])
        return ret
 

        