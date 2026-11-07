class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def bfs(i,j):
            area = 0
            queue = deque([(i,j)])
            visited.add((i,j))

            while queue:
                r,c = queue.popleft()
                area += 1
                directions = [(r+1,c),(r-1,c),
                             (r,c+1), (r,c-1)]
                for nr, nc in directions:
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return area
        
        maxArea = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    cur = bfs(r,c)
                    maxArea = max(maxArea, cur)
        return maxArea
