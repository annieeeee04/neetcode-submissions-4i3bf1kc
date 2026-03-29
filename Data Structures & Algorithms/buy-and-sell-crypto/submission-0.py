class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        buy = prices[0]
        
        for p in prices[1:]:
            if p < buy:
                buy = p
            else:
                profit = p - buy
                max_profit = max(max_profit, profit)
        
        return max_profit