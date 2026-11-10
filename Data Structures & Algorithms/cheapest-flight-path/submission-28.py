class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,p in flights:
            graph[u].append((v, p))
        cache = {}

        def dfs(node, stops):
            if node == dst:
                return 0
            if stops == 0:
                return float('inf')
            if (node, stops) in cache:
                return cache[(node, stops)]
            
            min_cost = float('inf')
            for nb, w in graph[node]:
                res = dfs(nb, stops-1)
                if res != float('inf'):
                    min_cost = min(min_cost, res + w)
            cache[(node, stops)] = min_cost 
            return cache[(node, stops)]
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1
