class Solution {
    // [idx, currsum] stores the ways
    int[][] dp;
    int totalSum;
    public int findTargetSumWays(int[] nums, int target) {
        // 
        int currSum = 0;
        // { [idx, currSum(before applying idx)] : numOfWays}
        totalSum = 0;
        for (int i: nums){
            totalSum += i;
        }
        dp = new int[nums.length][2 * (totalSum) + 1];
        
        for (int i = 0; i < nums.length; i ++){
            for (int j = 0 ; j < 2 * totalSum + 1; j ++){
                dp[i][j] = -1;
            }
        }

        return recurse(0, 0, nums, target);
    }
    // returns
    public int recurse(int idx, int currSum, int[] nums, int target){
        //currSum is the sum before current index
        int currSumIdx = currSum + totalSum;
        if (idx == nums.length){
            if (currSum == target){
                return 1;
            }
            return 0;
        }

if (currSumIdx < 0 || currSumIdx > 2 * totalSum) {
    return 0;
}
        if (dp[idx][currSumIdx] != -1){
            return dp[idx][currSumIdx];

        }
        dp[idx][currSumIdx] = recurse(idx + 1, currSum + nums[idx], nums, target) + recurse(idx + 1 , currSum - nums[idx], nums, target);
        
        return dp[idx][currSumIdx];
    }
}
