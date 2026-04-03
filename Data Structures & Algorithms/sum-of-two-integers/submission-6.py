class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ret = 0
        for i in range(32):
            
            ai = ((a >> i ) & 1)
            bi = (b >> i) & 1
            carrynext = 0
            if carry == 0:
                carrynext = ai & bi
            else:
                carrynext = ai | bi
            
            ai = ai ^ carry
            carry = carrynext
            bit = ai ^ bi
            bit = bit << i
            ret = ret | bit
            #carry on hte next if carry = 0 and both are 1, or if carry = 1 and there is a 1
        if ret & (1 << 31):
            ret -= 1 << 32
        return ret
