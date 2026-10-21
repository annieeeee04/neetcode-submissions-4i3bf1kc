class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v,t))
        minHeap = []
        time = 0
        minHeap.append((0, k))
        visited = set()

        while minHeap:
            t1, cur = heapq.heappop(minHeap)
            if cur in visited:
                continue
            visited.add(cur)
            time = max(time, t1)
            for nb, t2 in graph[cur]:
                if nb not in visited:
                    heapq.heappush(minHeap, (t1+t2, nb))

        return time if len(visited) == n else -1