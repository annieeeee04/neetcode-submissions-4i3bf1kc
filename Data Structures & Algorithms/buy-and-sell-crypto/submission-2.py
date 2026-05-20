class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]

        profit = 0
        best = 0
        for p in prices[1:]:
            if p < buy:
                buy = p
            else:
                profit = p - buy
                best = max(best, profit)
        return best