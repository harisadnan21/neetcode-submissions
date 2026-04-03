from collections import Counter
class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        retlst = []
        freqmap = Counter(s)
        l = 0
        r = 0
        print(freqmap)
        
        ##l == r only at the start of a new window / substring
        # we consider r a part of the string here
        currwindow = {}
        currchars = set()
        while l < len(s):
            if s[r] not in currwindow:
                currwindow[s[r]] = 0
            currwindow[s[r]] += 1
            currchars.add(s[r])

            allCharsIterated = True

            for char in currchars:
                if currwindow[char] != freqmap[char]:
                    allCharsIterated = False
            
            if allCharsIterated:
                #split
                retlst.append(r - l + 1)
                l = r + 1
                r = l
                currchars.clear()
            else:
                r += 1

        return retlst


        