class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0,0)]
        total = 0
        visited = set()

        while minHeap:
            c, idx = heapq.heappop(minHeap)
            if idx in visited:
                continue
            visited.add(idx)
            total += c

            for i in range(len(points)):
                if i not in visited:
                    dist = (abs(points[idx][0] - points[i][0]) +
                           abs(points[idx][1] - points[i][1]))
                    heapq.heappush(minHeap, [dist, i])
        return total