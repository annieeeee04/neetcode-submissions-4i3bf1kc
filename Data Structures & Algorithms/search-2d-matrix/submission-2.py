class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        l, r = 0, ROW*COL-1

        while l <= r:
            mid = (l+r) // 2
            row = mid // COL
            col = mid % COL
            key = matrix[row][col]

            if key == target:
                return True
            elif key < target:
                l += 1
            else:
                r -= 1
        return False