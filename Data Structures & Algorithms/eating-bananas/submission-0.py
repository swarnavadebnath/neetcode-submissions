class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        l=1
        r=m
        res=r
        while l<=r:
            k = (l+r)//2
            t=0
            for p in piles:
                t+=math.ceil(float(p)/k)
            if t<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res




        