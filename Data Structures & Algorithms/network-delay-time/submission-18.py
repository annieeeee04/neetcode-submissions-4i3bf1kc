class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = [(0,k)]
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append([v,t])
        visited = set()
        time = 0
        
        while minHeap:
            t1, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, t1)

            for nb, t2 in graph[node]:
                if nb not in visited:
                    heapq.heappush(minHeap, (t1+t2, nb))
        
        return time if len(visited) == n else -1