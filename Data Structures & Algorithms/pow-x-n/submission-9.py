class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recurse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 2:
                return x * x
            if n % 2:
                return x * recurse(x, n -1)
            return recurse(x, n//2) ** 2

        answer = recurse(x, abs(n))
        if n < 0:
            return 1 / answer
        return answer
