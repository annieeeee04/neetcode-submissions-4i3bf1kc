class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, cur, remaining):
            if remaining == 0:
                res.append(cur.copy())

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                val = candidates[i]
                if val > remaining:
                    break
                cur.append(val)
                dfs(i + 1, cur, remaining - val)
                cur.pop()
        
        dfs(0, [], target)
        return res