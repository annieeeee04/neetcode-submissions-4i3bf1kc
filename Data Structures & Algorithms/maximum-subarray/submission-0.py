class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] >= nums[r] + cur:
                l = r
                cur = nums[r]
            else:
                cur += nums[r]
            max_sum = max(cur, max_sum)
        
        return max_sum