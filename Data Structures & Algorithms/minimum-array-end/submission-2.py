class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n-=1
        res = x
        bitpos = 0
        while n>0:
            if (x & (1<<bitpos)) == 0:
                Nbit = (n & 1)
                res |= (Nbit<<bitpos)
                n>>=1
            bitpos+=1
        return res
        