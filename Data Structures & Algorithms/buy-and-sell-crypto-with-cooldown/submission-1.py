# Use Memoization 
# Time: O(n)
# Space: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # states: buying/selling or cooldown
        # if Buying -> i + 1
        # if Selling(not Buying) -> i + 2 (forced cooldown)
        dp = {} # (idx, buying?) -> max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        
        return dfs(0, True)