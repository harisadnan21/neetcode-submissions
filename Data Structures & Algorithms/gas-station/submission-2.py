class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        index = 0
        currgas = 0
        for i, a in enumerate(range(len(gas))):
            currgas += gas[i]
            if currgas < cost[i]:
                # cant go to the next gas station
                currgas =0
                index = i + 1
            else:
                # we have enough gas to get to the next station
                currgas -= cost[i]
        return index
             
