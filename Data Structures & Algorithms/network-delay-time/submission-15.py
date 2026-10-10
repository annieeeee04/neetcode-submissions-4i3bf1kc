class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        visited = set()
        t = 0
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            t1, cur = heapq.heappop(minHeap)
            if cur in visited:
                continue
            visited.add(cur)
            t = max(t, t1)
            for v,t2 in graph[cur]:
                if v not in visited:
                    heapq.heappush(minHeap, (t1+t2, v))
        return t if len(visited) == n else -1