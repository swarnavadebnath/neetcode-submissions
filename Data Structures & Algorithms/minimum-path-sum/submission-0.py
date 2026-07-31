class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[float('inf')]*(col+1) for _ in range(row+1)]
        dp[row-1][col] = 0
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                dp[r][c] = grid[r][c] + min(dp[r+1][c],dp[r][c+1])
        return dp[0][0]

        