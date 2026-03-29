class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(m,n):
            stack = []
            stack.append((m,n))
            seen.add((m,n))
            while stack:
                m,n = stack.pop()
                directions = [(m+1,n), (m-1,n), (m,n+1), (m,n-1)]
                for (r,c) in directions:
                    if (r in range(ROW) and 
                        c in range(COL) and
                        (r,c) not in seen and 
                        grid[r][c] == '1'):
                        seen.add((r,c))
                        stack.append((r,c))

        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in seen and grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        return res 