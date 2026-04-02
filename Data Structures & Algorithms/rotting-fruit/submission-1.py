class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0: return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            time += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1

        return time if fresh == 0 else -1