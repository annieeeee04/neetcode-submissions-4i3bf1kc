class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacs, atls = set(), set()
        ROW, COL = len(heights), len(heights[0])

        def dfs(i,j,visited,prev):
            if (i not in range(ROW) or
                j not in range(COL) or
                (i,j) in visited or
                heights[i][j] < prev):
                return
            
            visited.add((i,j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        for r in range(ROW):
            dfs(r, 0, pacs, heights[r][0])
            dfs(r, COL - 1, atls, heights[r][COL-1])
        for c in range(COL):
            dfs(0, c, pacs, heights[0][c])
            dfs(ROW-1, c, atls, heights[ROW-1][c])
    
        out = []
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in pacs and (i,j) in atls:
                    out.append((i,j))
        return out