class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ROW, COL = len(grid), len(grid[0])
        max_area = 0

        def bfs(m,n,area):
            queue = deque()
            queue.append((m,n))
            seen.add((m,n))
            while queue:
                row, col = queue.popleft()
                directions = [(row+1, col), (row, col+1), 
                            (row-1, col), (row, col-1)]
                for (r, c) in directions:
                    if (r in range(ROW) and 
                        c in range(COL) and
                        (r,c) not in seen and
                        grid[r][c] == 1):
                        queue.append((r,c))
                        seen.add((r,c))
                        area += 1
            return area
        
        for m in range(ROW):
            for n in range(COL):
                if grid[m][n] == 1 and (m,n) not in seen:
                    seen.add((m,n))
                    area = bfs(m,n,1)
                    max_area = max(max_area, area)
        return max_area

