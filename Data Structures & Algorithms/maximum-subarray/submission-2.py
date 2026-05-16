class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        cur = 0
        for r in range(len(nums)):
            if nums[r] + cur < nums[r]:
                cur = nums[r]
            else:
                cur += nums[r]
            best = max(best, cur)
        return best