class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []

        def backtrack(i, path, remaining):
            if remaining == 0:
                out.append(path[:])

            for j in range(i, len(nums)):
                val = nums[j]
                if val > remaining:
                    break
                path.append(nums[j])
                backtrack(j, path, remaining - val)
                path.pop()
                
        backtrack(0, [], target)
        return out