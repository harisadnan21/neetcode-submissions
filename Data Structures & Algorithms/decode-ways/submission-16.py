class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":  
            return 0  # Edge case: If the string starts with "0", it's invalid

        oneBefore = 1  # Ways to decode last character (base case)
        twoBefore = 1  # Ways to decode an empty string (base case)
        curr = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0  # "0" cannot be decoded alone
            else:
                curr = oneBefore  # Single-digit decoding
            
                if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:  
                    curr += twoBefore  # Two-digit decoding
            
            twoBefore = oneBefore
            oneBefore = curr

        return curr