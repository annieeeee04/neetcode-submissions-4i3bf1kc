class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        # all oranges are rotten or there's no orange
        if fresh == 0: return 0

        time = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:
            # process entire current level at once
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1  # ← increment ONCE per round, not per cell
        
        return time if fresh == 0 else -1