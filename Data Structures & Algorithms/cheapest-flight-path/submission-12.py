class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {} # node, stops to dst
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v,p))

        def dfs(i, stops):
            if i == dst:
                return 0
            
            if stops == 0:
                return float('inf')
            
            if (i, stops) in cache:
                return cache[(i, stops)]
            
            min_cost = float('inf')
            for neighbor, p in graph[i]:
                res = dfs(neighbor, stops-1)
                if res != float('inf'):
                    min_cost = min(min_cost, p + res)
            cache[(i, stops)] = min_cost
            return cache[(i, stops)]
        res = dfs(src, k+1)
        return res if res != float('inf') else -1