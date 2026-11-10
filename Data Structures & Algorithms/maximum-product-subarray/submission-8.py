class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minP, maxP = nums[0], nums[0]
        best = nums[0]
        for n in nums[1:]:
            options = [n, n*minP, n*maxP]
            maxP = max(options)
            minP = min(options)
            best = max(best, maxP)
        return best