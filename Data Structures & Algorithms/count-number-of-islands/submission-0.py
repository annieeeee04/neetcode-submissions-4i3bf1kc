class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        num = 0
        seen = []

        def bfs(m, n):
            queue = deque()
            queue.append((m,n))
            seen.append((m,n))

            while queue:
                row, col = queue.popleft()
                directions = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
                for (r, c) in directions:
                    if (r in range(ROW) and 
                        c in range(COL) and 
                        (r, c) not in seen and 
                        grid[r][c] == '1'):
                        queue.append((r, c))
                        seen.append((r, c))
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1' and (r,c) not in seen:
                    num += 1
                    bfs(r, c)
        return num