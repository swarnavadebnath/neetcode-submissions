class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*n
        def dfs(i):
            if i == len(s):
                return True
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    if dp[j] == False:
                        dp[j] = dfs(j+1)
        dfs(0)
        return dp[n-1]
        