# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Base case: entire first row and first col = 1
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                # the sum of path coming from the 
                # left and above
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]