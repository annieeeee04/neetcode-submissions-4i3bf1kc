class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for s in stones:
            for i in range(target, s-1, -1):
                dp[i] = dp[i-s] or dp[i]
        
        for t in range(target, -1, -1):
            if dp[t]:
                return total - t * 2