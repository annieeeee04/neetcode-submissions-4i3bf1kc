class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
        