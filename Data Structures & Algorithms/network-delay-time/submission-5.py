class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        heapq.heappush(minHeap, (0, k)) # time, node
        visited = set()
        graph = defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((ti, vi))

        time = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = t1

            for t2, v2 in graph[n1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (t1+t2, v2))
        
        return time if len(visited) == n else -1