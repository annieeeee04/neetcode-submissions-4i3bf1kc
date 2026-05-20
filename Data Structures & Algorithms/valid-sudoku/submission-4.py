class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                key = board[i][j]

                if key == '.':
                    continue

                box_idx = (i // 3) * 3 + (j // 3)

                if (key in row_set[i] or 
                    key in col_set[j] or
                    key in box_set[box_idx]):
                    return False
                
                row_set[i].add(key)
                col_set[j].add(key)
                box_set[box_idx].add(key)
        return True

