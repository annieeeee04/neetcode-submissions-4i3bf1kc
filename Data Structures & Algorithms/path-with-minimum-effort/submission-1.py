class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        minHeap = [[0, 0, 0]]
        minEffort = 0
        visited = set()
        ROW, COL = len(heights), len(heights[0])

        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r == ROW-1 and c == COL-1):
                return effort

            directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for nr, nc in directions:
                if (nr in range(ROW) and
                    nc in range(COL) and
                    (nr, nc) not in visited):
                    step = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(minHeap, (max(effort, step), nr,nc))
        
        return 0