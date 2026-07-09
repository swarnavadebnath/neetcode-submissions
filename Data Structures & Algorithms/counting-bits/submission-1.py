class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1,n+1):
            c = 0
            while i:
                i = i & (i-1)
                c+=1
            res.append(c)
        return res
        