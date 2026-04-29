class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        if fresh == 0: return 0

        time = 0
        while queue and fresh != 0:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                for nr, nc in directions:
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
                        
        return time if fresh == 0 else -1
