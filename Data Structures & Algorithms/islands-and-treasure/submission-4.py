class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 2147483647):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            dist += 1