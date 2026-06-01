class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        s=[]
        for i in range(len(temp)):
            c=0
            t=temp[i]
            while (i+c)<len(temp):
                if temp[i+c]>t:
                    s.append(c)
                    break
                if (i+c)==len(temp)-1:
                    s.append(0)
                c+=1
        return s
                

        