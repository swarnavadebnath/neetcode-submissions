class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res=[]
        for i in ops:
            c=len(res)
            if i=="+":
                res.append(res[c-1]+res[c-2])
            elif i=="C":
                res.pop()
            elif i=="D":
                res.append(2*res[c-1])
            else:
                res.append(int(i))
        s=0
        for i in res:
            s+=i
        return s



        