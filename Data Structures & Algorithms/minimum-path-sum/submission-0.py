class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dp = [[float('inf')] * (COL + 1) for _ in range(ROW + 1)]
        dp[0][1] = 0
        
        for r in range(1, ROW+1):
            for c in range(1, COL+1):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r-1][c-1]
        return dp[ROW][COL]