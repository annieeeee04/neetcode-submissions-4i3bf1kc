class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def bfs(i,j):
            visited.add((i,j))
            queue = deque()
            queue.append((i,j))
            
            while queue:
                r,c = queue.popleft()
                directions = [(r+1,c),(r-1,c),
                             (r,c+1), (r,c-1)]
                for dr, dc in directions:
                    if (dr in range(ROW) and
                        dc in range(COL) and 
                        (dr, dc) not in visited and
                        grid[dr][dc] == '1'):
                        visited.add((dr,dc))
                        queue.append((dr,dc))
        num = 0
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in visited and grid[i][j] == '1':
                    bfs(i,j)
                    num += 1
        return num