class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for r in range(1, self.m+1):
            for c in range(1, self.n+1):
                self.dp[r][c] = (self.matrix[r-1][c-1] +
                                 self.dp[r-1][c] + 
                                 self.dp[r][c-1] - 
                                 self.dp[r-1][c-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.dp[row2+1][col2+1] - 
                self.dp[row2+1][col1] -
                self.dp[row1][col2+1] +
                self.dp[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)