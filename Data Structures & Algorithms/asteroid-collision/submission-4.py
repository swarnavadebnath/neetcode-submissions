class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        s=[]
        for a in ast:
            while s and s[-1]>0 and a<0:
                if s[-1]<abs(a):
                    s.pop()
                    continue
                elif s[-1]==abs(a):
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(a)
        return s

            

        
        