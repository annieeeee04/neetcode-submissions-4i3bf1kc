class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r not in range(ROW) or
                c not in range(COL) or 
                (r,c)  in visited or
                board[r][c] != word[i]):
                return False
            
            visited.add((r,c))
            res = (backtrack(r+1, c, i+1) or
                   backtrack(r-1, c, i+1) or
                   backtrack(r, c+1, i+1) or
                   backtrack(r, c-1, i+1))
            visited.remove((r,c))
            return res

        for i in range(ROW):
            for j in range(COL):
                if backtrack(i,j,0): return True
        return False
                