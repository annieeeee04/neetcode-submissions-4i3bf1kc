class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {}  # (point, stops) -> minimum cost to reach dst
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        def dfs(node, stops):
            if node == dst:
                return 0
            if stops == 0:
                return float('inf')
            if (node, stops) in cache:
                return cache[(node, stops)]
            
            min_cost = float('inf')
            for neighbor, cost in graph[node]:
                result = dfs(neighbor, stops-1)
                if result != float('inf'):
                    min_cost = min(min_cost, result + cost)
            cache[(node, stops)] = min_cost
            return min_cost
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1

