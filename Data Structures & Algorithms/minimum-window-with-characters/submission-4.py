class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for c in t:
            if c in need:
                need[c]+=1
            else:
                need[c]=1
        def isSub(s2):
            have={}
            for c in s2:
                if c in have:
                   have[c]+=1
                else:
                    have[c]=1
            for c in need:
                if have.get(c,0)<need[c]:
                     return False
            return True
        l=0
        r=0
        s2=""
        res=s+" "
        if len(t)>len(s):
            return ""
        if s==t:
            return s
        while r<len(s):
            s2+=s[r]
            while isSub(s2):
                if len(res)>len(s2):
                    res=s2
                s2=s2[1:]
            r+=1
        if res==s+" ":
         return ""
        else:
            return res
            



        