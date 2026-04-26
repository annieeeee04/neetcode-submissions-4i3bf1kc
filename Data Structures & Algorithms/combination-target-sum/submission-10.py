class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(i, path, remaining):
            if remaining == 0:
                out.append(path[:])
            
            for j in range(i, len(nums)):
                if nums[j] > remaining:
                    break
                
                path.append(nums[j])
                backtrack(j, path, remaining - nums[j])
                path.pop()
        
        backtrack(0, [], target)
        return out