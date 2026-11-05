class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for s in stones:
            for t in range(target, s-1, -1):
                dp[t] = dp[t] or dp[t-s]
        
        for t in range(target, -1, -1):
            if dp[t]:
                return total - 2 * t