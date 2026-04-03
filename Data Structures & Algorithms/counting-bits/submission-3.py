class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0 for i in range(n +1)]
        currCeiling = 4
        for i in range(1,len(arr)):
            if i >= currCeiling:
                currCeiling *= 2
             
            arr[i] += 1 + arr[i - currCeiling // 2]
        
        return arr 