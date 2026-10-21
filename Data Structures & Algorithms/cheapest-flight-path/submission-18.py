class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {}
        graph = defaultdict(list)
        for u,v,p in flights:
            graph[u].append((v, p))
        
        def dfs(i, total):
            if i == dst:
                return 0
            if total == 0:
                return float('inf')
            if (i, total) in cache:
                return cache[(i, total)]
            
            minCost = float('inf')
            for nb, cost in graph[i]:
                res = dfs(nb, total - 1)
                if res != float('inf'):
                    minCost = min(minCost, cost + res)
            cache[(i, total)] = minCost
            return cache[(i, total)]
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1