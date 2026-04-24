# Time: O(n) , n is the number of grids
# Space: O(n)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                key = board[r][c]
                if key == '.':
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3)

                if (key in rowSets[r] or
                    key in colSets[c] or
                    key in boxSets[box_idx]):
                    return False
                else:
                    rowSets[r].add(key)
                    colSets[c].add(key)
                    boxSets[box_idx].add(key)
        return True