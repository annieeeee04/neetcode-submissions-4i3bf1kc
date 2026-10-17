class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        best = nums[0]
        cur = 0

        for r in range(len(nums)):
            if nums[r] + cur <= nums[r]:
                l = r 
                cur = nums[r]
            else:
                cur += nums[r]
            best = max(best, cur)
        return best