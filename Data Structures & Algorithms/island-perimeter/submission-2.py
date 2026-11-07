class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    res += 4
                    if r > 0 and grid[r-1][c] == 1:
                        res -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        res -= 2
        return res
                        