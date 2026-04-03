from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        retlst = []

        def checkPalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start, currlst):
            if start == len(s):
                retlst.append(currlst[:])
                return
            for end in range(start, len(s)):
                w = s[start:end + 1]
                if checkPalindrome(w):
                    currlst.append(w)
                    backtrack(end + 1, currlst)
                    currlst.pop()

        backtrack(0, [])
        return retlst