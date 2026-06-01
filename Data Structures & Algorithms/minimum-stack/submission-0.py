class MinStack:

    def __init__(self):
        self.l=[]
        self.m=[]
        

    def push(self, val: int) -> None:
        self.l.append(val)
        val=min(val,self.m[-1] if self.m else val)
        self.m.append(val)

        

    def pop(self) -> None:
        self.l.pop()
        self.m.pop()
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.m[-1]

        
