class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n):
            if n == 0:
                return 1
            if n <0:
                return 0
            return rec(n-1) +rec(n-2)
        return rec(n)