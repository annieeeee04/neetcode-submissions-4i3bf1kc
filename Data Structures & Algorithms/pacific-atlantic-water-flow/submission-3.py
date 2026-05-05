class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacs, atls = set(), set()

        def dfs(i, j, visited, prev):
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                (i,j) in visited or
                heights[i][j] < prev):
                return
            
            visited.add((i,j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
        
        for r in range(ROWS):
            dfs(r, 0, pacs, heights[r][0])
            dfs(r, COLS-1, atls, heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0, c, pacs, heights[0][c])
            dfs(ROWS-1, c, atls, heights[ROWS-1][c])
        
        out = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacs and (i,j) in atls:
                    out.append((i,j))
        return out