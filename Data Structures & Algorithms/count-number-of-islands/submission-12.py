class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            stack = [(i,j)]
            visited.add((i,j))

            while stack:
                i,j = stack.pop()
                directions = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for ni, nj in directions:
                    if (ni in range(m) and
                        nj in range(n) and
                        (ni,nj) not in visited and
                        grid[ni][nj] == '1'):
                        stack.append((ni,nj))
                        visited.add((ni,nj))
        
        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    cnt += 1
        return cnt