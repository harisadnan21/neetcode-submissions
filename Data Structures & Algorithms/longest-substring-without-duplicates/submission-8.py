class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        dic = {}
        maxl = 0
        
        while r < len(s):
            if s[r] in dic:
                #char exists already in substring
                l = max(dic[s[r]] + 1, l)
                
                dic[s[r]] = r


            else:
                dic[s[r]] = r

            
            currlen = r -l + 1
            if currlen > maxl:
                maxl = currlen
            print(l, r, maxl, s[l: r])
            r = r + 1

            
        return maxl


        