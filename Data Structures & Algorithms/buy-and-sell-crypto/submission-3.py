class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best = 0
        buy = float('inf')
        for p in prices:
            if p < buy:
                buy = p
            else:
                profit = p - buy
            best = max(best, profit)
        return best