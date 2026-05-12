class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = []
        heapq.heappush(minHeap, (0, 0))
        visited = set()

        best = 0
        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            best += cost

            for j in range(n):
                if j not in visited:
                    dist = (abs(points[i][0] - points[j][0]) + 
                            abs(points[i][1] - points[j][1]))
                    heapq.heappush(minHeap, (dist, j))
        return best