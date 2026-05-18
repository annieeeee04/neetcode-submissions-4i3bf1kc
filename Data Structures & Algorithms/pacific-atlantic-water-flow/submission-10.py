# Iterative version very flurry

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacs, atls = set(), set()
        ROW, COL = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        q1, q2 = deque(), deque()

        for r in range(ROW):
            q1.append((r, 0, heights[r][0]))
            pacs.add((r,0))
            q2.append((r, COL-1, heights[r][COL-1]))
            atls.add((r, COL-1))
        for c in range(COL):
            q1.append((0, c, heights[0][c]))
            pacs.add((0,c))
            q2.append((ROW-1, c, heights[ROW-1][c]))
            atls.add((ROW-1, c))

        while q1:
            r, c, prev = q1.popleft()

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if (nr in range(ROW) and
                    nc in range(COL) and
                    (nr, nc) not in pacs and
                    heights[nr][nc] >= prev):
                    pacs.add((nr, nc))
                    q1.append((nr, nc, heights[nr][nc]))

        while q2:
            r, c, prev = q2.popleft()

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if (nr in range(ROW) and
                    nc in range(COL) and
                    (nr, nc) not in atls and
                    heights[nr][nc] >= prev):
                    atls.add((nr, nc))
                    q2.append((nr, nc, heights[nr][nc]))

        out = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacs and (r,c) in atls:
                    out.append((r,c))
        return out
