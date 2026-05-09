class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW, COL = len(matrix), len(matrix[0])
        l, r    = 0, COL-1  # left/right → column boundaries
        up, down = 0, ROW-1 # up/down   → row boundaries
        out = []

        while l <= r and up <= down:
            # top row → left to right
            for i in range(l,r+1):
                out.append(matrix[up][i])
            up += 1
            # right col → top to bottom
            for i in range(up, down+1):
                out.append(matrix[i][r])
            r -= 1
            # bottom row → right to left
            if up <= down:
                for i in range(r, l-1, -1):
                    out.append(matrix[down][i])
                down -= 1
            # left col → bottom to top
            if l <= r:
                for i in range(down, up-1, -1):
                    out.append(matrix[i][l])
                l += 1
        return out