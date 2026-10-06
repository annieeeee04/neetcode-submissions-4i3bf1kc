class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visited,prev):
            if (r not in range(ROW) or
                c not in range(COL) or
                heights[r][c] < prev or 
                (r,c) in visited):
                return
            
            visited.add((r,c))
            directions = ((r+1,c),(r-1,c),(r,c+1),(r,c-1))
            for dr,dc in directions:
                dfs(dr,dc,visited,heights[r][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, atl, heights[r][COL-1])
        for c in range(COL):
            dfs(0, c, pac, heights[0][c]) 
            dfs(ROW-1, c, atl, heights[ROW-1][c])
        
        out = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    out.append((r,c))
        
        return out