# Time: O(n^4) worst case for backtracking
# Space: O(1) extra (plus output)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(i, remaining, total, path):
            nonlocal out
            if remaining == 0:
                if total == target:
                    out.append(path[:])
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                path.append(nums[j])
                backtrack(j+1, remaining-1, total + nums[j], path)
                path.pop()
        
        backtrack(0, 4, 0, [])
        return out