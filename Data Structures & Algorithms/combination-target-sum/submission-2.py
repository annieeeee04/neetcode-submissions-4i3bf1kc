class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path.copy())
            
            for j in range(start, len(nums)):
                val = nums[j]
                if val > remaining:
                    break
                
                path.append(val)
                dfs(j, path, remaining-val)
                path.pop()

        dfs(0, [], target)
        return res