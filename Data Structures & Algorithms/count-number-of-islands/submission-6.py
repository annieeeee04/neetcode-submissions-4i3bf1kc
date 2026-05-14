# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        stack = []

        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        def dfs(i,j):
            stack.append((i,j))
            visited.add((i,j))

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr in range(ROW) and
                        nc in range(COL) and
                        grid[nr][nc] == '1' and 
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        stack.append((nr, nc))
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in visited and grid[i][j] == '1':
                    cnt += 1
                    dfs(i,j)
        return cnt