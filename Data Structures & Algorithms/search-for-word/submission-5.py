class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        seen = set()
        
        def dfs(m,n,i):
            if i == len(word):
                return True
            
            if (m not in range(ROW) or 
                n not in range(COL) or
                (m,n) in seen or
                board[m][n] != word[i]):
                return False
            
            seen.add((m,n))
            found = (dfs(m+1,n,i+1) or
                    dfs(m-1, n, i+1) or
                    dfs(m, n+1, i+1) or
                    dfs(m, n-1, i+1))
            seen.remove((m,n))
            return found
        
        for i in range(ROW):
            for j in range(COL):
                if dfs(i,j, 0):
                    return True
        return False