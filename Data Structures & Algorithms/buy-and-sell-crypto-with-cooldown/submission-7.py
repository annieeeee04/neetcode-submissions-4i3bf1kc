# Time: O(n)
# Space: O(n)
# 状态 (i, buying) 表示第 i 天、当前能买还是能卖；
# cool 就是什么都不做，状态不变，只有交易才会翻转 buying，卖出后多跳一天作为冷冻期

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                cache[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                cache[(i, buying)] = max(sell, cooldown)
            
            return cache[(i, buying)]
        
        return dfs(0, True)