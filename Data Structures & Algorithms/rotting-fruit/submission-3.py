class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        fresh = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        if fresh == 0: return 0

        time = 0
        while queue and fresh > 0:
            time += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr in range(ROW) and 
                        nc in range(COL) and
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in seen):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
                        fresh -= 1
        return time if fresh == 0 else -1
