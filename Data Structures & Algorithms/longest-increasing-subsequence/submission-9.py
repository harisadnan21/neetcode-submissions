class Solution:
    def __init__(self):
        self.maxNum = 0
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def recurse(prev_sub_len, greatest_num_prev, curr_idx):
            if curr_idx == len(nums):
                self.maxNum = max(self.maxNum, prev_sub_len)
                return
            # Include current number if it's greater
            if nums[curr_idx] > greatest_num_prev:
                recurse(prev_sub_len + 1, nums[curr_idx], curr_idx + 1)
            
            # Skip current number
            recurse(prev_sub_len, greatest_num_prev, curr_idx + 1)

        recurse(0, float('-inf'), 0)
        return self.maxNum
        