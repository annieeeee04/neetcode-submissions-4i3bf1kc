class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        if fresh == 0: return 0

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        time = 0
        while queue and fresh > 0:
            time += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

        return time if fresh == 0 else -1