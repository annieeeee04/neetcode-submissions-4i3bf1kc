class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        minHeap = []
        graph = defaultdict(list)
        for ui,vi,ti in times:
            graph[ui].append([vi,ti])
        
        heapq.heappush(minHeap, [0,k])
        t = 0
        while minHeap:
            t1, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, t1)
            for nb, t2 in graph[node]:
                if nb not in visited:
                    heapq.heappush(minHeap, [t1+t2, nb])
        
        return t if len(visited) == n else -1
                    