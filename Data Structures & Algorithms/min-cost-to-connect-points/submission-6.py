# V = number of points
# The graph is fully connected — 
# every point connects to every other point → V² edges
# Each heap push is O(log(heap size)) = O(log V²) = O(log V)
# → Time: O(V² log V)

# Heap can hold up to V² entries (one per edge)
# Space: O(V²)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [] # cost, idx
        heapq.heappush(minHeap, (0, 0))
        visited = set()
        
        total = 0
        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            total += cost

            for j in range(len(points)):
                if j not in visited:
                    dist = (abs(points[i][0] - points[j][0]) + 
                            abs(points[i][1] - points[j][1]))
                    heapq.heappush(minHeap, (dist, j))
        return total 
