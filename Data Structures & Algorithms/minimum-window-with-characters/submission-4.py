class Solution:
    from collections import defaultdict, Counter
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        dic_t = Counter(t)
        window = defaultdict(int)
        required = len(dic_t)
        formed = 0
        min_len = float('inf')
        l = 0
        substring_idx = [0,0]
        for r, char in enumerate(s):
            window[char] +=1
            
            if char in dic_t and window[char] == dic_t[char]:
                formed += 1
            
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r-l + 1
                    substring_idx = [l, r]

                # move l right
                window[s[l]] -=1
                if s[l] in dic_t and window[s[l]] < dic_t[s[l]]:
                    formed -=1
                
                l +=1 

        return "" if min_len == float("inf") else s[substring_idx[0] : substring_idx[1] + 1]


        