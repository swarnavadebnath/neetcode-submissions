class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        Cs,Ct={},{}
        for i in range(len(s)):
            Cs[s[i]] = 1+ Cs.get(s[i],0)
            Ct[t[i]] = 1+ Ct.get(t[i],0)
        return Cs==Ct

        