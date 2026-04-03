class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        retlst = []
        dic = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        def backtrack(idx, currstring):
            if idx > len(digits) -1:
                retlst.append(currstring)
                return
            strdig = digits[idx]

            for char in dic[strdig]:
                backtrack(idx + 1, currstring + char)
        backtrack(0, "")  
        return retlst        

        