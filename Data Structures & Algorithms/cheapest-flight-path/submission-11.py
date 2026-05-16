# Time: O(k * E)

# cache: (number of unique cities) * (number of possible stop values)
# Space: O(n * k) 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # in each stop, we are making decisions of where to go
        # so cache can help reducing the duplicate path
        cache = {}
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v,p))

        def dfs(i, stop):
            # start == end -> 0 travel needed
            if i == dst:
                return 0
            # cannot travel anymore but didn't reach dst
            if stop == 0:
                return float('inf') # flag of failure
            
            if (i, stop) in cache:
                return cache[(i,stop)]
            
            min_cost = float('inf')
            for neighbor, p in graph[i]:
                res = dfs(neighbor, stop - 1)
                if res != float('inf'):
                    min_cost = min(min_cost, res + p)
            cache[(i, stop)] = min_cost
            return cache[(i, stop)]
        
        res = dfs(src, k+1)
        return res if res != float('inf') else -1