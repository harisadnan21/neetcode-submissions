class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = x
        if n == 0:
            return 1
        count = 1

        while count < abs(n):
            ret *= x
            count +=1
        print(count)
        print(ret)
        if n > 0:
            return ret   
        else:
            return (1/ ret)     
       