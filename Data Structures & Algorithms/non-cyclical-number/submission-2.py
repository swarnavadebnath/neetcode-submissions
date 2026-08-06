class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        temp = n
        while True:
            vis.add(temp)
            s = 0
            while temp>0:
                s = s + (temp%10)**2
                temp//=10
            if s == 1:
                return True
            if s in vis:
                return False
            temp = s
