class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        l = min(l1,l2)
        s=""
        for i in range(l):
            s+=word1[i]+word2[i]
        if l1>l2:
            s+=word1[l:]
        else:
            s+=word2[l:]
        return s


        