class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTime = 0
        minHeap = [[0, k]]
        visited = set()

        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v, t))

        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            minTime = max(minTime, t)

            for nb, w in graph[node]:
                if nb not in visited:
                    heapq.heappush(minHeap, (w + t, nb))
        return minTime if len(visited) == n else -1