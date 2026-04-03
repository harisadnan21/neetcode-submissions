class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        retlen = 0 
        if len(s) ==1 or len(s) == 0:
            return s
        
        for i in range(len(s) -1):
            # stops at 2nd last index
            currLen = 1 
            left = i
            right = i
            while left > -1 and right < len(s) and s[left] == s[right]:
                #keep on looping with char at middle , check for palindrome
                currLen = right - left + 1
                if currLen > retlen:
                    ret = s[left : right +1]
                    retlen = currLen
                left -= 1
                right +=1

            left = i 
            right= i + 1
            while left > -1 and right < len(s) and s[left] == s[right]:
                currLen = right - left + 1
                if currLen > retlen:
                    ret = s[left : right +1]
                    retlen = currLen
                left -= 1
                right +=1
                

            
        return ret

        