class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {}
        graph = defaultdict(list)
        for u,v,t in flights:
            graph[u].append([v, t])

        def dfs(i, stops):
            if i == dst:
                return 0
            if stops == 0:
                return float('inf')
            if (i, stops) in cache:
                return cache[(i, stops)]
            
            minCost = float('inf')
            for nb, extra in graph[i]:
                res = dfs(nb, stops-1)
                if res != float('inf'):
                    minCost = min(minCost, extra + res)
            cache[(i, stops)] = minCost
            return cache[(i, stops)]
        
        out = dfs(src, k+1)
        return out if out != float('inf') else -1