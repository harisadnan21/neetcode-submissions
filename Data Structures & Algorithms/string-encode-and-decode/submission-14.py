class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if not strs:
            return ""

        for i, a in enumerate(strs):
            ret += str(len(a))
            ret += ","
        ret += "#"
        for i, a in enumerate(strs):
            ret += a
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        numLst = []
        retlst = []
        i = 0 
        while s[i] != "#":
            y = i
            while s[y] != ",":
                y +=1
            numLst.append(int(s[i : y]))
            i = y +1
        i += 1
        for ind, a in enumerate(numLst):
            retlst.append(s[i:i + a])
            i +=a


        return retlst
            

        

                    

