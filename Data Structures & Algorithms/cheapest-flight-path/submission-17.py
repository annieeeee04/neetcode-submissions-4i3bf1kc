class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {}
        graph = defaultdict(list)
        for u,v,p in flights:
            graph[u].append((v,p))
        
        def dfs(i, stop):
            if i == dst:
                return 0
            if stop == 0:
                return float('inf')
            if (i,stop) in cache:
                return cache[(i,stop)]
            
            minCost = float('inf')
            for nb,p in graph[i]:
                res = dfs(nb, stop-1)
                if res != float('inf'):
                    minCost = min(minCost, res+p)
            cache[(i,stop)] = minCost
            return cache[(i,stop)] 
        
        out = dfs(src, k+1)
        return out if out!=float('inf') else -1