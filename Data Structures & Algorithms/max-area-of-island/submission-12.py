class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def bfs(i,j):
            area = 0
            queue = deque()
            queue.append((i,j))

            while queue:
                i, j = queue.popleft()
                area += 1
                directions = [(i+1,j), (i-1,j),
                              (i,j+1), (i,j-1)]
                for di,dj in directions:
                    if (di in range(ROW) and
                        dj in range(COL) and
                        (di,dj) not in visited and
                        grid[di][dj] == 1):
                        queue.append((di,dj))
                        visited.add((di,dj))
            return area
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    area = bfs(r,c)
                    res = max(res, area)
        return res