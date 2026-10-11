class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin, best = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            options = (x, x * curMax, x * curMin) 
            curMax = max(options)
            curMin = min(options)
            best = max(best, curMax)
        return best