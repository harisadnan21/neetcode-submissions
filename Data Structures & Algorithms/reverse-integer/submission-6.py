class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = - (2 ** 31)
        sign = -1 if x < 0 else 1
        ret = 0
        x = abs(x)

        while x:
            remainder = x % 10
            x //= 10
            if (ret > INT_MAX // 10) or ( (ret == INT_MAX//10) and (remainder >INT_MAX % 10 )) :
                return 0
    
            ret = (ret * 10) + remainder 
        
        return ret * sign