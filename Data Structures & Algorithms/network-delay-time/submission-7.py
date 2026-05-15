class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        
        minHeap = []
        heapq.heappush(minHeap, (0, k)) # cost, node
        visited = set()

        total = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            total = cost

            for neighbor, time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time+cost, neighbor))
        
        return total if len(visited) == n else -1
                    