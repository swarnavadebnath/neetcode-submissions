class Solution:
    def decodeString(self, s: str) -> str:
        l=[]
        for i in s:
            if i!=']':
                l.append(i)
            else:
                sub=""
                while l[-1]!='[':
                    sub=l.pop()+sub
                l.pop()
                k=""
                while l and l[-1].isdigit():
                    k=l.pop()+k
                l.append(int(k)*sub)
        return "".join(l)
                


        