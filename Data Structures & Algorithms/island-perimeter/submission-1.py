# Time: O(m * n)
# Space: O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        out = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    out += 4
                    if r > 0 and grid[r-1][c] == 1:
                        out -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        out -= 2
        return out