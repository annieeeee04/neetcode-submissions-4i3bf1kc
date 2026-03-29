class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        max_area = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(m,n,area):
            stack = []
            stack.append((m,n))
            seen.add((m,n))

            while stack:
                r,c = stack.pop()
                area += 1
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for (nr, nc) in directions:
                    if (nr in range(ROW) and 
                        nc in range(COL) and
                        (nr, nc) not in seen and 
                        grid[nr][nc] == 1):
                        stack.append((nr,nc))
                        seen.add((nr,nc))
            return area

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and (i,j) not in seen:
                    area = dfs(i,j,0)
                    max_area = max(area, max_area)
        return max_area