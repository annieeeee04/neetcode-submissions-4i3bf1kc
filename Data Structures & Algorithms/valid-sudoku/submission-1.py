class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rowSets = [set() for _ in range(n)]
        colSets = [set() for _ in range(n)]
        boxSets = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                key = board[r][c]
                if key == '.':
                    continue
                    
                box_idx = (r // 3) * 3 + (c // 3)
                
                if (key in boxSets[box_idx] or 
                    key in rowSets[r] or 
                    key in colSets[c]):
                    return False
                else:
                    boxSets[box_idx].add(key)
                    rowSets[r].add(key)
                    colSets[c].add(key)
        
        return True