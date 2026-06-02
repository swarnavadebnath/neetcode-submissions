class FreqStack:

    def __init__(self):
        self.s=[]
        self.d={}
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if val in self.d:
            self.d[val]+=1
        else:
            self.d[val]=1
        

    def pop(self) -> int:
        m=max(self.d.values())
        v=0
        for i in range(len(self.s)-1,-1,-1):
            if self.d[self.s[i]]==m:
                v=self.s.pop(i)
                self.d[v]-=1
                break
        return v

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()