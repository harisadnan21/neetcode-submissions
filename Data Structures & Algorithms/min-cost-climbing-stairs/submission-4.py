class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lidxmincost = 0
        llidxmincost = 0
        if len(cost) == 2:
            return min(cost[0], cost[1])
        for i in range(2, len(cost)):
            costofreaching = min(lidxmincost + cost[i-1], llidxmincost + cost[i-2])
            llidxmincost =lidxmincost
            lidxmincost = costofreaching
        
        return min(lidxmincost + cost[-1], llidxmincost + cost[-2])         
        