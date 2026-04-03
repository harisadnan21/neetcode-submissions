class Solution:
    def isHappy(self, n: int) -> bool:
        numbersSeen= set()
        def nextNumber(n):
            currsum = 0
            while n != 0:
                remainder = n % 10
                n = n // 10
                currsum += remainder**2

            return currsum
        while n not in numbersSeen:
            if n ==1:
                return True
            numbersSeen.add(n)
            n = nextNumber(n)
        return False
        
        