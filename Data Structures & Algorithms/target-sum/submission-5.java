class Solution {

    public int findTargetSumWays(int[] nums, int target) {
        // 
        int currsum = 0;
        int ret = 0;
        return recurse(0, 0, nums, target);
    }
    // returns
    public int recurse(int idx, int currSum, int[] nums, int target){
        //currSum is the sum before current index
        if (idx >= nums.length) {
            if (currSum == target){
                return 1;
            }
            return 0;
        }
        
        return recurse(idx + 1, currSum + nums[idx], nums, target) + recurse(idx + 1 , currSum - nums[idx], nums, target);
    }
}
