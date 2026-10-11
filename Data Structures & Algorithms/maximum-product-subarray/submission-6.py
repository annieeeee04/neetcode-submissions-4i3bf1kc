# Time: O(n)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = best = nums[0]
        for x in nums[1:]:
            options = (x, x * curMax, x * curMin)    # uses the old curMax / curMin
            curMax, curMin = max(options), min(options)
            best = max(best, curMax)
        return best

        # 中文：同时维护以当前位置结尾的最大和最小乘积，因为负数会让最小值翻成最大值