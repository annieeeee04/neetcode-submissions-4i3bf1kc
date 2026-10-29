class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, 0)]
        visited = set()

        res = 0
        while minHeap:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += cost

            for j in range(len(points)):
                if j not in visited:
                    dist = (abs(points[i][0]-points[j][0]) + 
                            abs(points[i][1]-points[j][1]))
                    heapq.heappush(minHeap, (dist, j))
        return res