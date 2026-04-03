class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            c = (n >> i) & 1
            count += c

        return count
        