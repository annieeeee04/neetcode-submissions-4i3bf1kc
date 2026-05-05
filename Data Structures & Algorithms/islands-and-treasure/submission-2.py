# multi-source BFS
# guarantees the first time you reach a cell = shortest distance
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None
        
        ROW, COL = len(grid), len(grid[0])
        queue = deque()

        # Step 1: enqueue all treasure chests as starting points
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    queue.append((i,j))

        # Step 2: BFS outward from all chests simultaneously
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr in range(ROW) and 
                    nc in range(COL) and
                    grid[nr][nc] == 2147483647): # only unvisited land cells
                    grid[nr][nc] = grid[r][c] + 1 # distance from chest
                    queue.append((nr,nc))
            