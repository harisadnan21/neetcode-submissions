class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        idx1 = False
        idx2 = False
        idx3 = False
        newTriplets = []
        for elem in triplets:
            if (elem[0]> target[0]) or (elem[1]>target[1]) or (elem[2]>target[2]):
                continue
            newTriplets.append(elem)
        
        for elem in newTriplets:
            if elem[0] == target[0]:
                idx1 = True
            if elem[1] == target[1]:
                idx2 = True
            if elem[2] == target[2]:
                idx3= True

        return idx1 and idx2 and idx3

        