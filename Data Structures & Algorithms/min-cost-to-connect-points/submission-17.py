class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, 0)]
        visited = set()
        minCost = 0
        n = len(points)

        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            minCost += cost

            for j in range(n):
                if j not in visited:
                    diff = (abs(points[i][0] - points[j][0]) + 
                            abs(points[i][1] - points[j][1]))
                    heapq.heappush(minHeap, (diff, j))
        return minCost