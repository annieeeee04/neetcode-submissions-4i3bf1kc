class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        seen = []

        def dfs(m, n, i):
            if i == len(word):
                return True
            
            if (m < 0 or n < 0 or
                m == ROW or n == COL or 
                (m,n) in seen or 
                board[m][n] != word[i]):
                return False
            
            seen.append((m, n))
            found = (
                dfs(m+1, n, i+1) or 
                dfs(m, n+1, i+1) or 
                dfs(m-1, n, i+1) or 
                dfs(m, n-1, i+1) 
            )
            seen.remove((m,n))
            return found
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False