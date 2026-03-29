class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, total, path):
            if total == target:
                res.append(path[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            backtrack(i+1, total + candidates[i], path)
            path.pop()
            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i = i + 1
            backtrack(i+1, total, path)
        
        backtrack(0, 0, [])
        return res