class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))

        prices = [float('inf')] * n
        q = deque([(0, src, 0)])

        while q:
            c1, node, stops = q.popleft()
            if stops > k:
                continue
            
            for nb, c2 in graph[node]:
                newCost = c1 + c2
                if newCost < prices[nb]:
                    prices[nb] = newCost
                    q.append([newCost, nb, stops + 1])
        return prices[dst] if prices[dst] != float('inf') else -1