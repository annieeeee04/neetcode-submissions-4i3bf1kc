# Time: O(E log N)
# Space: O(E + N)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for ui, vi, ti in times:
            graph[ui].append((vi,ti))
        minHeap = []
        heapq.heappush(minHeap, (0,k)) # time, node
        visited = set()

        t = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:  # ✅ skip stale entries
                continue
            visited.add(n1)    # ✅ mark on pop
            t = t1
            for v2, t2 in graph[n1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (t1+t2, v2))
        
        return t if len(visited) == n else -1
