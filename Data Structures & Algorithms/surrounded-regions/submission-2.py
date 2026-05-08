class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or
                    r == ROWS-1 or c == COLS-1) and board[r][c] == 'O':
                    q.append((r,c))
        
        seen = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r,c = q.popleft()
            board[r][c] = 'S'
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if (nr in range(ROWS) and
                    nc in range(COLS) and
                    (nr,nc) not in seen and
                    board[nr][nc] == 'O'):
                    q.append((nr,nc))
                    seen.add((nr,nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'