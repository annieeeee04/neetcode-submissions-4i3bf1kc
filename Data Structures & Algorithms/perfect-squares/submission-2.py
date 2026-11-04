class Solution:
    def numSquares(self, n: int) -> int:
        squares = [k * k for k in range(1, int(n ** 0.5) + 1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for x in range(1, n+1):
            for s in squares:
                if s > x:
                    break
                dp[x] = min(dp[x], dp[x-s] + 1)
        return dp[n]
