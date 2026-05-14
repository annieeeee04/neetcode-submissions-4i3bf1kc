class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        dpMax, dpMin = [1] * n, [1] * n
        dpMax[0] = dpMin[0] = nums[0]
        globalMax = nums[0]

        for i in range(1, n):
            options = [nums[i], nums[i] * dpMax[i-1], nums[i] * dpMin[i-1]]
            dpMax[i] = max(options)
            dpMin[i] = min(options)
            globalMax = max(globalMax, dpMax[i])
        return globalMax