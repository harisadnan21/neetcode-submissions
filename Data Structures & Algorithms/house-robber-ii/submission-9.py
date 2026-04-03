class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]

        if len(nums) == 1:
            return nums[0]
        list1 = [0 for i in range(len(nums))]
        list2 = [0 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            #including the first number, excluding the last
            includingMax = nums[i] if i >= len(nums) -3 else nums[i]+ list1[i + 2]
            excludingMax = 0 if i >= len(nums) -2 else list1[i + 1]
            list1[i] = max(includingMax, excludingMax)
            # list1[i] = max(list[i] + list[i + 2], list[i + 1])

        for i in range(len(nums)- 1, 0, - 1):
            includingMax = nums[i] if i >= len(nums) - 2 else nums[i] + list2[i + 2]
            excludingMax = 0 if i >= len(nums) - 1 else list2[i + 1]
            list2[i] = max(includingMax,excludingMax)

        return max([max(list1), max(list2)])
        