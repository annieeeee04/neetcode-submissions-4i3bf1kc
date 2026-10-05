class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        ROW, COL = len(grid), len(grid[0])

        def bfs(r,c,area):
            queue = deque()
            queue.append((r,c))
            
            while queue:
                area += 1
                r,c = queue.popleft()
                seen.add((r,c))

                directions = ((r+1,c), (r-1,c),
                              (r,c+1), (r,c-1))
                for dr,dc in directions:
                    if (dr in range(ROW) and
                        dc in range(COL) and
                        (dr,dc) not in seen and
                        grid[dr][dc] == 1):
                        seen.add((dr,dc))
                        queue.append((dr,dc))
            return area
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in seen and grid[r][c] == 1:
                    cur = bfs(r,c,0)
                    ans = max(ans, cur)
        return ans