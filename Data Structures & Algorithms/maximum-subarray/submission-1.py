class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        l = 0

        for r in range(len(nums)):
            if nums[r] >= nums[r] + curSum:
                l = r
                curSum = nums[r]
            else:
                curSum += nums[r]
            maxSum = max(maxSum, curSum)
        
        return maxSum