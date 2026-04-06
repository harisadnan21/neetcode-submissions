class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == len(s) and j == len(p):
                return True
            if j==len(p):
                return False
            
            #handle * by looking ahead
            if j + 1 < len(p) and p[j + 1] == "*":
                #handle for 1 or more
                ans = recurse(i, j + 2)
                if i < len(s) and (p[j] == "." or s[i] == p[j]):
                    ans = ans or recurse(i + 1, j)
                dp[(i, j)] = ans
                return ans

            
            #handle normal case
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                ans = recurse(i + 1, j + 1)
                dp[(i, j)] = ans
                return ans
            
            dp[(i, j)] = False
            return False

        return recurse(0, 0)