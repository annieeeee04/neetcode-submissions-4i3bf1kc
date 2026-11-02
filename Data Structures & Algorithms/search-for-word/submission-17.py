class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def bfs(r,c,i):
            if (r not in range(ROW) or
                c not in range(COL) or
                (r,c) in visited or
                board[r][c] != word[i]):
                return False
                
            if i == len(word)-1: return True

            visited.add((r,c))
            res = (bfs(r+1,c,i+1) or
                   bfs(r-1,c,i+1) or
                   bfs(r,c+1,i+1) or
                   bfs(r,c-1,i+1))
            visited.remove((r,c))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if bfs(r,c,0): return True
        return False
                