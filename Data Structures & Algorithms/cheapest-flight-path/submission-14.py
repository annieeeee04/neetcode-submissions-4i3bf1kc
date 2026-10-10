class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {}
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v,p))
        
        def dfs(i, stop):
            if i == dst:
                return 0
            if stop == 0:
                return float('inf')
            
            if (i,stop) in cache:
                return cache[(i,stop)]
            
            min_cost = float('inf')
            for neighbor, p in graph[i]:
                res = dfs(neighbor, stop-1)
                if res != float('inf'):
                    min_cost = min(min_cost, p + res)
            cache[(i, stop)] = min_cost
            return cache[(i, stop)]
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1