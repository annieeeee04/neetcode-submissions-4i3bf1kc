class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        for i in range(k+1):
            temp = dp.copy()

            for u, v , price in flights:
                if dp[u] == float('inf'):
                    continue
                if dp[u] + price < temp[v]:
                    temp[v] = dp[u] + price
            dp = temp
        
        return dp[dst] if dp[dst] != float('inf') else -1