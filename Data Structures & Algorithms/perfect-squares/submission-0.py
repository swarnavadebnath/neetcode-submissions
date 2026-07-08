import math
class Solution:
    def numSquares(self, n: int) -> int:
        lim = int(math.sqrt(n))
        nums = []
        for i in range(1,lim+1):
            nums.append(i**2)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for num in nums:
                if i-num>=0:
                    dp[i] = min(dp[i],1+dp[i-num])
        return dp[n]
        
