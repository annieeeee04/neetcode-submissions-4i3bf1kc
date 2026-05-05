class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # flow inward from the oceans
        # check if it's uphill
        def dfs(r, c, visited, prev):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in visited or
                heights[r][c] < prev):
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])           # Pacific left border
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # Atlantic right border
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])         # Pacific top border
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # Atlantic bottom border
        
        out = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    out.append((r,c))
        return out