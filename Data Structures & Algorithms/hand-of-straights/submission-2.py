class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        

        freqMap = {}
        for elem in hand:
            if elem not in freqMap:
                freqMap[elem] = 0

            freqMap[elem] +=1
        
        hand.sort()
        for val in hand:
            if freqMap[val]== 0:
                continue
            # pick this as the start and decrement its group
            for elem in range(val, groupSize + val):
                if elem not in freqMap or freqMap[elem] == 0:
                    return False
                freqMap[elem]-=1
        return True
