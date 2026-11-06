class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            if r == ROW - 1 and c == COL - 1 and obstacleGrid[r][c] != 1:
                return 1

            res = 0
            if r < ROW and c < COL and obstacleGrid[r][c] != 1:
                res = dfs(r+1, c) + dfs(r, c+1)
            cache[(r,c)] = res
            return cache[(r,c)]
        
        return dfs(0,0)