class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = best = nums[0]
        for n in nums[1:]:
            options = [n, n*curMax, n*curMin]
            curMax = max(options)
            curMin = min(options)
            best = max(curMax, best)
        return best