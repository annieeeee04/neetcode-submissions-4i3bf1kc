class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        def backtrack(i, left, path):
            if left == 0:
                out.append(path[:])
            
            for j in range(i, n+1):
                path.append(j)
                backtrack(j+1, left-1, path)
                path.pop()
        backtrack(1, k, [])
        return out