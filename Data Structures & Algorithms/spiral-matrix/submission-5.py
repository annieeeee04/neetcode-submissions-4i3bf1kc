class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW, COL = len(matrix), len(matrix[0])
        l, r = 0, COL-1
        up, down = 0, ROW-1
        out = []

        while l <= r and up <= down:
            # l -> r, top row
            for col in range(l, r+1):
                out.append(matrix[up][col])
            up += 1

            # up -> down, right col
            for row in range(up, down+1):
                out.append(matrix[row][r])
            r -= 1

            if up <= down:
                for col in range(r, l-1, -1):
                    out.append(matrix[down][col])
                down -= 1
            if l <= r:
                for row in range(down, up-1, -1):
                    out.append(matrix[row][l])
                l += 1
        return out