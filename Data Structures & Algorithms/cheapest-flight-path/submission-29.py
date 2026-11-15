# Time: O(k * E)
# Space: O(N * k + E)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        memo = {}
        graph = defaultdict(list)
        for u,v,p in flights:
            graph[u].append((v, p))

        def dfs(i, stops):
            if i == dst:
                return 0
            if stops == 0:
                return float('inf')
            if (i, stops) in memo:
                return memo[(i, stops)]
            
            minP = float('inf')
            for nb, p in graph[i]:
                res = dfs(nb, stops - 1)
                if res != float('inf'):
                    minP = min(minP, res + p)
            memo[(i, stops)] = minP
            return memo[(i, stops)]
        
        out = dfs(src, k+1)
        return out if out != float('inf') else -1