# graph: O(N + E),cache: O(N × k), recursion stack: O(k)
# Time : O(E * K), sparse graph: E = N, dense graph: E = N^2
# Space: O(E + N*K)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cache = {} # (node, stops) -> min cost to reach dst
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))

        def dfs(i, stop):
            if i == dst:
                return 0
            if stop == 0:
                return float('inf')
            if (i, stop) in cache:
                return cache[(i, stop)]
            
            min_cost = float('inf')
            for neighbor, price in graph[i]:
                result = dfs(neighbor, stop - 1)
                if result != float('inf'):
                    min_cost = min(min_cost, result + price)
            cache[(i, stop)] = min_cost
            return min_cost
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1