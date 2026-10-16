class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        cur = 0
        best = float('-inf')

        for r in range(len(nums)):
            if cur + nums[r] <= nums[r]:
                l = r
                cur = nums[r]
            else:
                cur += nums[r]
            best = max(best, cur)
        return best