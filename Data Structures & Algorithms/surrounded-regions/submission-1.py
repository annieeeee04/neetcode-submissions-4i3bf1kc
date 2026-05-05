class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        stack = []

        def capture(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return

            board[r][c] = 'S'

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or j == 0 or 
                    i == ROWS-1 or j == COLS-1) and board[i][j] == 'O':
                    capture(i,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
        
        

