class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None
        
        ROW, COL = len(grid), len(grid[0])
        queue = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    queue.append((i,j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr in range(ROW) and 
                    nc in range(COL) and
                    grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
            