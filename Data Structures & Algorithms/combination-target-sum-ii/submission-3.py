class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def backtrack(i, path, remaining):
            if remaining == 0:
                out.append(path[:])
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                val = candidates[j]
                if val > remaining:
                    break
                
                path.append(val)
                backtrack(j+1, path, remaining-val)
                path.pop()

        backtrack(0,[],target)
        return out