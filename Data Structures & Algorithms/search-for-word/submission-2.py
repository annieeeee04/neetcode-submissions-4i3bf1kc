class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        seen = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (c == COL or r == ROW or
                c < 0 or r < 0 or
                board[r][c] != word[i] or
                (r,c) in seen):
                return False

            seen.add((r,c))
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            seen.remove((r,c))
            return found
        
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False