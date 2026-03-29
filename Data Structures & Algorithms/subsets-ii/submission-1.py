class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # all subsets that includes nums[i]
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
            # all subsets that excludes nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, path)
        
        dfs(0, [])
        return res