class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(i, path, remaining):
            if remaining == 0:
                ans.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > remaining:
                    break
                
                path.append(candidates[j])
                backtrack(j+1, path, remaining-candidates[j])
                path.pop()

        backtrack(0, [], target)
        return ans