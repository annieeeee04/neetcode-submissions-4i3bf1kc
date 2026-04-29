class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        seen = set()
        ROW, COL = len(grid), len(grid[0])
        stack = []

        def dfs(i,j):
            seen.add((i,j))
            stack.append((i,j))

            while stack:
                r, c = stack.pop()
                seen.add((r,c))
                directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                for nr, nc in directions:
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        (nr,nc) not in seen and
                        grid[nr][nc] == '1'):
                        seen.add((nr,nc))
                        stack.append((nr,nc))
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in seen and grid[i][j] == '1':
                    num += 1
                    dfs(i,j)
        return num