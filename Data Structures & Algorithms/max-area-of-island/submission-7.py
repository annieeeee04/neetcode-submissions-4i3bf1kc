class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        stack = []

        best = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i,j):
            stack.append((i,j))
            visited.add((i,j))
            area = 0

            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (nr in range(ROW) and 
                        nc in range(COL) and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1):
                        stack.append((nr, nc))
                        visited.add((nr, nc))
            return area
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in visited and grid[i][j] == 1:
                    cur = dfs(i,j)
                    best = max(best, cur)
        return best