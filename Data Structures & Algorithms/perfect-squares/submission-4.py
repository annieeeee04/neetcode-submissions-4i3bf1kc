class Solution:
    def numSquares(self, n: int) -> int:
        squares = [k * k for k in range(1, int(n ** 0.5) + 1)]
        dp = [n+1] * (n+1)
        dp[0] = 0

        for s in squares:
            for x in range(s, n+1):
                dp[x] = min(dp[x], dp[x-s] + 1)
        return dp[n]