class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                key = board[r][c]
                box = (r // 3) * 3 + (c // 3)
                if key == '.':
                    continue
                if (key in rowSet[r] or
                    key in colSet[c] or 
                    key in boxSet[box]):
                    return False
                
                rowSet[r].add(key)
                colSet[c].add(key)
                boxSet[box].add(key)
        return True