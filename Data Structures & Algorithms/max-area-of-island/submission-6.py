class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        maxArea = 0
        stack = []
        seen = set()

        def dfs(i,j,area):
            stack.append((i,j))
            seen.add((i,j))

            while stack:
                area += 1
                r, c = stack.pop()
                directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for nr, nc in directions:
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in seen):
                        seen.add((nr,nc))
                        stack.append((nr,nc))
            return area

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    cur = dfs(i,j,0)
                    maxArea = max(maxArea, cur)
        return maxArea