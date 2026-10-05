class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visit = set()

        def dfs(r,c,i):
            if (r not in range(ROW) or 
                c not in range(COL) or
                (r,c) in visit or
                board[r][c] != word[i]):
                return False
            
            if i == len(word)-1: return True

            visit.add((r,c))
            res = (dfs(r,c+1,i+1) or
                   dfs(r,c-1,i+1) or
                   dfs(r+1,c,i+1) or
                   dfs(r-1,c,i+1))
            visit.remove((r,c))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0): return True
        return False