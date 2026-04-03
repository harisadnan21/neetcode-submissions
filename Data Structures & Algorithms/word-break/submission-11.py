class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo= {}

        def recurse(l, r):
            if l == len(s):
                return True
            if r > len(s):
                return False
            currword = s[l :r]
            if (l , r) in memo:
                return memo[(l,r)]
            valRecurse = recurse(l , r + 1)
            if currword in wordSet:
                ans = recurse(r , r) or valRecurse
                memo[(l, r)] = ans
                return ans
            else:
                memo[(l,r)] = valRecurse
                return valRecurse
        
        return recurse(0, 0)
        