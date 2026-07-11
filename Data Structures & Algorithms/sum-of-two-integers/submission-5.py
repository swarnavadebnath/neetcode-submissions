class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxint = 0x7FFFFFF
        x = a & mask
        y = b & mask
        while y !=0:
            ans = (x^y) & mask
            carry = ((x & y)<<1) & mask
            x = ans
            y = carry
        if x>maxint:
            return ~(x^mask)
        else:
            return x
        