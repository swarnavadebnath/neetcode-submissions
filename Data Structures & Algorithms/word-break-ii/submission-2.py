class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        sub = []
        def dfs(i):
            if i == len(s):
                res.append(" ".join(sub))
                return
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    sub.append(w)
                    dfs(j+1)
                    sub.pop()
        dfs(0)
        return res
        