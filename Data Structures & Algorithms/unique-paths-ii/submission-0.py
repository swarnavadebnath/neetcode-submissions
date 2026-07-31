class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[row-1][col-1] == 1:
            return 0
        dp = [[0]*(col+1) for _ in range(row+1)]
        dp[row-1][col-1] = 1
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r+1][c]
                    dp[r][c] += dp[r][c+1]
        return dp[0][0]
                


        