class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount+1)
        # value -> num of coins need to achieve
        dp[0] = 0 # 0 coin needed to achieve 0, base case

        for a in range(1, amount + 1):
            for c in coins:
                # if the coin value is smaller than the value needed
                # continue working, otherwise skip this coin cuz its
                # value is too much
                if a - c >= 0:
                    dp[a] = min(dp[a-c]+1, dp[a])
        
        return dp[amount] if dp[amount] != amount + 1 else -1