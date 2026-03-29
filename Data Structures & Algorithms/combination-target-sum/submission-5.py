class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for j in range(i, len(nums)):
                if nums[j] > remaining:
                    return 

                path.append(nums[j])
                backtrack(j, path, remaining - nums[j])
                path.pop()
            
        backtrack(0, [], target)
        return res