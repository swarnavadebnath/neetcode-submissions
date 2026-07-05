class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        onestep = 1
        twostep = 1
        for i in range(2,n+1):
            cur = onestep + twostep
            twostep = onestep
            onestep = cur
        return cur
        