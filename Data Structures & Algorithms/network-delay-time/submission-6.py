class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        heapq.heappush(minHeap, (0, k)) # cost, node
        visited = set()
        graph = defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        cost = 0
        while minHeap:
            c1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            cost = c1

            for n2, c2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (c2+c1, n2))
        return cost if len(visited) == n else -1