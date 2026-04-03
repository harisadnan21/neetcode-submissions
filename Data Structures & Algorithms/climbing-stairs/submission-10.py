class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [0 for i in range(n)]

        def rec(n):
            if n == 0:
                return 1
            if n <0:
                return 0
            val1 = lst[n-1] if lst[n-1] != 0 else rec(n-1)
            val2 = lst[n-2] if lst[n-2] != 0 else rec(n-2)
            return val1 + val2

        
        return rec(n)