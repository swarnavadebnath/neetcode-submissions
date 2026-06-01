class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i=="+":
                v=s[-2]+s[-1]
                s.pop()
                s.pop()
                s.append(v)
            elif i=="-":
                 v=s[-2]-s[-1]
                 s.pop()
                 s.pop()
                 s.append(v)
            elif i=="*":
                 v=s[-2]*s[-1]
                 s.pop()
                 s.pop()
                 s.append(v)
            elif i=="/":
                 v=int(float(s[-2]/s[-1]))
                 s.pop()
                 s.pop()
                 s.append(v)
            else:
                s.append(int(i))
        return s[-1]

        