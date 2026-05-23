class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):
            if (r not in range(ROW) or
                c not in range(COL) or
                (r,c) in visited or
                board[r][c] != word[i]):
                return False

            if i == len(word) - 1: return True
            
            visited.add((r,c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            visited.remove((r,c))
            return res

        for i in range(ROW):
            for j in range(COL):
                if dfs(i,j,0): return True
        return False