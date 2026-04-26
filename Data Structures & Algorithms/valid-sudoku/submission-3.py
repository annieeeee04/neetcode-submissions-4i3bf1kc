class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                key = board[i][j]
                if key == '.':
                    continue

                boxIdx = (i // 3) * 3 + (j // 3)
                if (key in rowSets[i] or
                    key in colSets[j] or
                    key in boxSets[boxIdx]):
                    return False
                
                rowSets[i].add(key)
                colSets[j].add(key)
                boxSets[boxIdx].add(key)
        return True