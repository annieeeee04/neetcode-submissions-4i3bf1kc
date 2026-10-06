class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                directions = [(r+1,c), (r-1,c), (r, c+1), (r,c-1)]
                for dr, dc in directions:
                    if (dr in range(ROW) and
                        dc in range(COL) and
                        grid[dr][dc] == 1):
                        fresh -= 1
                        queue.append((dr,dc))
                        grid[dr][dc] = 2
            time += 1
        return time if fresh == 0 else -1