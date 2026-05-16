class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows, zeroCols = set(), set()
        ROW, COL = len(matrix), len(matrix[0])
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
        
        for r in zeroRows:
            for c in range(COL):
                matrix[r][c] = 0
        for c in zeroCols:
            for r in range(ROW):
                matrix[r][c] = 0
        