class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        span = 1
        n = len(self.stocks)
        for i in range(n-1, -1, -1):
            p = self.stocks[i]
            if p <= price:
                span += 1
            else:
                break
        self.stocks.append(price)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)