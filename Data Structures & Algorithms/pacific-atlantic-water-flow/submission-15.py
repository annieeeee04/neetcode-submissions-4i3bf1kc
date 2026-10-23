class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacs, atls = set(), set()
        ROW, COL = len(heights), len(heights[0])
        out = []
        def dfs(r,c,visited, prev):
            if (r not in range(ROW) or
                c not in range(COL) or
                (r,c) in visited or
                heights[r][c] < prev):
                return

            visited.add((r,c))
            directions = ((r+1,c),(r-1,c),(r,c+1),(r,c-1))
            for dr,dc in directions:
                dfs(dr,dc,visited,heights[r][c])

        for r in range(ROW):
            dfs(r, 0, pacs, heights[r][0])
            dfs(r, COL-1, atls, heights[r][COL-1])
        for c in range(COL):
            dfs(0, c, pacs, heights[0][c])
            dfs(ROW-1, c, atls, heights[ROW-1][c])
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in pacs and (i,j) in atls:
                    out.append((i,j))
        return out
