class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        sq=0
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            elif m*m>x:
                r=m-1
            else:
                sq=m
                l=m+1
        return sq
        