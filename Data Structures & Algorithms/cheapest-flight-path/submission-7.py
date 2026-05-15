class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        cache = {}
        def dfs(i, stop):
            if i == dst:
                return 0
            if stop == 0:
                return float('inf')
            if (i, stop) in cache:
                return cache[(i, stop)]

            minCost = float('inf')
            for neighbor, price in graph[i]:
                result = dfs(neighbor, stop-1)
                if result != float('inf'):
                    minCost = min(minCost, result + price)
            cache[(i, stop)] = minCost
            return minCost

        res = dfs(src, k+1)
        return res if res != float('inf') else -1