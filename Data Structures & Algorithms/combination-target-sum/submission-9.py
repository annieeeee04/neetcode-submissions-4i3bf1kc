class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
            
            for j in range(start, len(nums)):
                if nums[j] > remaining:
                    break
                
                path.append(nums[j])
                backtrack(j, path, remaining - nums[j])
                path.pop()
        
        backtrack(0, [], target)
        return res