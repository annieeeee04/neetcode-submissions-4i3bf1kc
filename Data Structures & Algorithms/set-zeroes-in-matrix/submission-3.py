# Time: O(m*n)
# Space: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows, zero_cols = set(), set()
        ROW, COL = len(matrix), len(matrix[0])

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in range(ROW):
            for c in range(COL):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
        