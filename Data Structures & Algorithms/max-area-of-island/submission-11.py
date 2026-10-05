# Time: O(m · n), each cell enqueued once, O(1) set lookups
# Space: O(m · n), for seen (the queue holds at most one frontier)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        ROW, COL = len(grid), len(grid[0])

        def bfs(r,c):
            queue = deque([(r, c)])
            # Mark the start cell before the loop instead of at pop time
            # every other cell was already marked on push
            seen.add((r, c))
            area = 0
            
            while queue:
                area += 1
                r,c = queue.popleft()

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
                    cur = bfs(r,c)
                    ans = max(ans, cur)
        return ans