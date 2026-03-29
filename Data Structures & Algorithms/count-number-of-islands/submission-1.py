class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        num = 0
        seen = []

        def bfs(m, n):
            queue = deque()
            queue.append((m,n))

            while queue:
                (r,c) = queue.popleft()
                seen.append((r,c))

                for (nr, nc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if (nr in range(ROW) and 
                        nc in range(COL) and
                        grid[nr][nc] == '1' and 
                        (nr, nc) not in seen):
                        queue.append((nr, nc))
                        seen.append((nr, nc))
        
        cnt = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1' and (i, j) not in seen:
                    cnt += 1
                    bfs(i, j)
        return cnt