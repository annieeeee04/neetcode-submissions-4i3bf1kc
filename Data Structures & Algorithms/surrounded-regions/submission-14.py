class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        queue = deque()
        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or c == 0 or
                    r == ROW-1 or c == COL-1) and board[r][c] == 'O':
                    queue.append((r,c))
                    board[r][c] = 'S'
        
        while queue:
            r,c = queue.popleft()
        
            directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for nr,nc in directions:
                if (nr in range(ROW) and
                    nc in range(COL) and
                    board[nr][nc] == 'O'):
                    queue.append((nr,nc))
                    board[nr][nc] = 'S'
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
