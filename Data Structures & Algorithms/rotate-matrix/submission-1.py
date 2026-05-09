# Time: O(m*n)
# Space: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])
        # transpose the matrix 
        for r in range(ROW):
            for c in range(r+1, COL): # only work on the upper triangle
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # flip horizontally
        for r in range(ROW):
            matrix[r].reverse()