class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    
        directions = [(1,0), (0,1),(-1,0),(0,-1)]
        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr in range(ROW) and
                    nc in range(COL) and
                    grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
