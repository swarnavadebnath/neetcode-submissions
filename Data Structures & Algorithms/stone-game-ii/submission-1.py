class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        n = len(piles)
        suffix = [0]*n
        suffix[n-1] = piles[n-1]
        for j in range(n-2,-1,-1):
            suffix[j] = piles[j] + suffix[j+1] 
        def dfs(i,m):
            if i>=len(piles):
                return 0
            if (i,m) in dp:
                return dp[(i,m)]
            c = 0
            for x in range(1,min(2*m,len(piles)-i)+1):
                c = max(c,suffix[i] - dfs(i+x,max(m,x)))
            dp[(i,m)] = c
            return dp[(i,m)]
        return dfs(0,1)

        