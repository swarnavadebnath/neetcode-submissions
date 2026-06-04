class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        k=len(s1)
        for i in range(k,len(s2)+1):
            sub = s2[i-k:i]
            sub = "".join(sorted(sub))
            if sub==s1:
                return True
        return False 


        