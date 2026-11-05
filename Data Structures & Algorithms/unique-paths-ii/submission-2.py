class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r == ROW-1 and c == COL-1 and obstacleGrid[r][c] != 1:
                return 1
            
            res = 0
            if r < ROW and c < COL and obstacleGrid[r][c] != 1:
                res = dfs(r+1,c) + dfs(r, c+1)
            memo[(r,c)] = res
            return memo[(r,c)]
        
        return dfs(0,0)