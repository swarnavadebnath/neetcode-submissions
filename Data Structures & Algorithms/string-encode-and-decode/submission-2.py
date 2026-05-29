class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for c in strs:
            s+=c
            s+="."
        return s


    def decode(self, s: str) -> List[str]:
        l=[]
        s2=""
        for w in s:
            if w == ".":
                l.append(s2)
                s2=""
            else:
                s2+=w
        return l
        
