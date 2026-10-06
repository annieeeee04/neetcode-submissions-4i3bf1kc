class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None
            
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            r,c = queue.popleft()
            directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for dr,dc in directions:
                if (dr in range(ROW) and
                    dc in range(COL) and
                    grid[dr][dc] == 2147483647):
                    grid[dr][dc] = grid[r][c] + 1
                    queue.append((dr,dc))
