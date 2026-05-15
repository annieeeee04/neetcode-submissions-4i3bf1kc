class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((vi,ti))
        
        minHeap = []
        heapq.heappush(minHeap, (0,k))
        visited = set()

        total = 0
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            total = cost
            visited.add(node)

            for neighbor, time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (time+cost, neighbor))
        return total if len(visited) == n else -1