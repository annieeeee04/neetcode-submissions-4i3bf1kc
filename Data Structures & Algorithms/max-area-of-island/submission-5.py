class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(m,n,area):
            stack = []
            stack.append((m,n))
            seen.add((m,n))
            while stack:
                area += 1
                m,n = stack.pop()
                directions = [(m+1,n), (m-1,n), (m,n+1), (m,n-1)]
                for (r,c) in directions:
                    if (r in range(ROW) and 
                        c in range(COL) and 
                        (r,c) not in seen and 
                        grid[r][c] == 1):
                        seen.add((r,c))
                        stack.append((r,c))
            return area
            
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in seen and grid[i][j] == 1:
                    area = dfs(i,j,0)
                    max_area = max(area, max_area)
        return max_area