class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {}
        graph = defaultdict(list)
        for u,v,t in flights:
            graph[u].append((v,t))
        
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
                if res < minCost:
                    minCost = min(minCost, res + cost)
            cache[(i, total)] = minCost
            return minCost
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1