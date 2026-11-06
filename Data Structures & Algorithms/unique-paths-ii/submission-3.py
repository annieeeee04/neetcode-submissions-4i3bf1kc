class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (COL+1) for _ in range(ROW+1)]
        dp[0][1] = 1

        for r in range(1, ROW+1):
            for c in range(1, COL+1):
                if obstacleGrid[r-1][c-1] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[ROW][COL]