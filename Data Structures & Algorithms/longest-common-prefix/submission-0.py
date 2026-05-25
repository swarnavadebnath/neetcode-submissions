class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        f = strs[0]
        l = strs[-1]
        i=0
        for c in f:
            if i<len(f) and i<len(l) and f[i]==l[i]:
                i+=1
        if i>0:
            return f[:i]
        else:
            return ""
        