class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        queue = deque()

        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or c == 0 or 
                    r == ROW - 1 or c == COL - 1) and board[r][c] == 'O':
                    queue.append((r,c))
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            r, c = queue.popleft()
            board[r][c] = 'S'

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if (nr in range(ROW) and
                    nc in range(COL) and
                    board[nr][nc] == 'O'):
                    queue.append((nr, nc))
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
        