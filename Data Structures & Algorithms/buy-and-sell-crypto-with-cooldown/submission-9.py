class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            res = 0
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                skip = dfs(i+1, buying)
                res = max(buy, skip)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                skip = dfs(i+1, buying)
                res = max(sell, skip)
            cache[(i, buying)] = res
            return cache[(i, buying)]
        
        return dfs(0, True)