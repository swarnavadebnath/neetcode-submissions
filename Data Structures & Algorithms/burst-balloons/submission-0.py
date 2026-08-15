class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new = [1]+nums+[1]
        dp = [[0]*(n+1) for _ in range(n+2)]
        for l in range(n,0,-1):
            for r in range(l,n+1):
                for i in range(l,r+1):
                    coins = new[l-1]*new[i]*new[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(coins,dp[l][r])
        return dp[1][n]


        