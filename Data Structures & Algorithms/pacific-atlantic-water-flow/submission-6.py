# Multi-source BFS
# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac_q, atl_q = deque(), deque()
        pacs, atls = set(), set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(ROWS):
            pac_q.append((r,0))
            pacs.add((r,0))
            atl_q.append((r,COLS-1))
            atls.add((r,COLS-1))

        for c in range(COLS):
            pac_q.append((0,c))
            pacs.add((0,c))
            atl_q.append((ROWS-1,c))
            atls.add((ROWS-1,c))
        
        def bfs(q, visited):
            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        (nr,nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr,nc))

        bfs(pac_q, pacs)
        bfs(atl_q, atls)

        out = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacs and (i,j) in atls:
                    out.append((i,j))
        return out