class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        num = 0
        seen = set()
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            
            while queue:
                r,c = queue.popleft()
                seen.add((r,c))
                diretions = [(r+1,c),(r-1,c),
                             (r,c+1), (r,c-1)]
                for m,n in diretions:
                    if (m in range(ROW) and
                        n in range(COL) and
                        (m,n) not in seen and
                        grid[m][n] == '1'):
                        queue.append((m,n))
                        seen.add((m,n))
            
        cnt = 0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in seen and grid[r][c] == '1':
                    cnt += 1
                    bfs(r,c)
        return cnt