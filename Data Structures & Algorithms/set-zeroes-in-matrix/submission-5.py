class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])
        isZeroCOl, isZeroRow = False, False
        for r in range(ROW):
            if matrix[r][0] == 0:
                isZeroCOl = True
        for c in range(COL):
            if matrix[0][c] == 0:
                isZeroRow = True
        
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, ROW):
            if matrix[r][0] == 0:
                for c in range(COL):
                    matrix[r][c] = 0
        for c in range(1, COL):
            if matrix[0][c] == 0:
                for r in range(ROW):
                    matrix[r][c] = 0
        
        if isZeroCOl:
            for r in range(ROW):
                matrix[r][0] = 0
        if isZeroRow:
            for c in range(COL):
                matrix[0][c] = 0
        