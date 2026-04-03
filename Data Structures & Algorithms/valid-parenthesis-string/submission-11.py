class Solution:
    def checkValidString(self, s: str) -> bool:
        brackstack = []
        starstack= []
        for i in range(len(s)):
            if s[i] == "(":
                brackstack.append(i)
            elif s[i] == "*":
                starstack.append(i)
            else:
                if not brackstack and not starstack:
                    return False
                if not brackstack:
                    starstack.pop()
                else:
                    brackstack.pop()
        print(brackstack)
        print(starstack)
        while brackstack:
            if len(brackstack) > len(starstack):
                return False
            brackidx = brackstack.pop()
            staridx = starstack.pop()
            if staridx < brackidx:
                return False
        return True
            
        