class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n stops -> n+1 edges
        dp = [float('inf')] * (n+1)
        dp[src] = 0   # cost to reach the stop

        for _ in range(k+1):
            temp = dp.copy()
            for u, v, p in flights:
                if dp[u] == float('inf'):
                    continue
                if dp[u] + p < temp[v]:
                    temp[v] = dp[u] + p
            dp = temp
        return dp[dst] if dp[dst] != float('inf') else -1