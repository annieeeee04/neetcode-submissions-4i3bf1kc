class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0,0,0)]
        ROW, COL = len(heights), len(heights[0])

        while minHeap:
            cost,r,c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (ROW-1,COL-1):
                return cost
            
            directions = [(r+1, c), (r-1, c), 
                           (r, c+1), (r, c-1)]
            for nr, nc in directions:
                if (nr in range(ROW) and
                    nc in range(COL) and
                    (nr,nc) not in visited):
                    diff = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(minHeap, (max(diff,cost), nr,nc))
        return 0