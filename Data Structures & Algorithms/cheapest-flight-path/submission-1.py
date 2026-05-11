# Time: O(k * E)
# Space: O(n)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k+1): # k stops = k+1 flights
            temp = prices.copy()

            for u, v, price in flights:
                # node u is UNREACHABLE so far
                if prices[u] == float('inf'):
                    continue
                if prices[u] + price < temp[v]:
                    temp[v] = prices[u] + price
            prices = temp
        
        return prices[dst] if prices[dst] != float('inf') else -1
