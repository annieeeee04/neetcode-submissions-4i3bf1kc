class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        board = [['.'] * n for i in range(n)]

        res = []
        def backtrack(r):
            if r == n:
                # flatten the matrix and save into a string
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                
                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                board[r][c] = '.'

        backtrack(0)
        return res
