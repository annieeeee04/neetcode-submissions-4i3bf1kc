class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][c]==0 for c in range(COL))
        first_col_zero = any(matrix[r][0]==0 for r in range(ROW))
        
        for r in range(1,ROW):
            for c in range(1,COL):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1,ROW):
            for c in range(1,COL):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if first_row_zero:
            for c in range(COL):
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(ROW):
                matrix[r][0] = 0