# Dijkstra
# each node’s time depends on the whole path from k, 
# so the heap key is cumulative (w1 + w2)
# Time: O(n log n) -> more informative:  O(E log N)
# Space: O(n) -> more informative: O(E + N)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        visited = set()
        minHeap = [(0, k)]
        minCost = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            minCost = max(minCost, cost)

            for nb, t in graph[node]:
                if nb not in visited:
                    heapq.heappush(minHeap, (t+cost, nb))
        return minCost if len(visited) == n else -1