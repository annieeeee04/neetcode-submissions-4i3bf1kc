class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        queue = deque()
        for r in range(ROW):
            for c in range(COL):
                if ((r == 0 or r == ROW-1 or
                    c == 0 or c == COL-1) and
                    board[r][c] == 'O'):
                    queue.append((r,c))
        
        while queue:
            r,c = queue.popleft()
            board[r][c] = 'S'

            directions = ((r+1,c),(r-1,c),(r,c+1),(r,c-1))
            for dr,dc in directions:
                if (dr in range(ROW) and 
                    dc in range(COL) and
                    board[dr][dc] == 'O'):
                    queue.append((dr,dc))
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
