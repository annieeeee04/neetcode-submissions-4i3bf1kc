class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in flights:
            graph[u].append((v,t))
        
        prices = [float('inf')] * n
        queue = deque([(0, src, 0)])

        while queue:
            cost, node, stops = queue.popleft()
            if stops > k:
                continue
            
            for nb, nbCost in graph[node]:
                newCost = nbCost + cost
                if newCost < prices[nb]:
                    prices[nb] = newCost
                    queue.append((newCost, nb, stops+1))
                
        return prices[dst] if prices[dst] != float('inf') else -1
