class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        out = 0
        seen = set()
        stack = []

        def dfs(r, c):
            seen.add((r,c))
            stack.append((r,c))

            while stack:
                r, c = stack.pop()
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for dr, dc in directions:
                    if (dr in range(ROW) and 
                        dc in range(COL) and
                        (dr, dc) not in seen and
                        grid[dr][dc] == '1'):
                        seen.add((dr,dc))
                        stack.append((dr, dc))
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in seen and grid[i][j] == '1':
                    out += 1
                    dfs(i, j)
        return out