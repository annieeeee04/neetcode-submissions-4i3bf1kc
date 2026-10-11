# Forward version
# Time: O(n²)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n        # dp[i] = LIS ending at i
        for i in range(n):  # forward: dp[j] with j < i is already final
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # 中文：dp[i] 是以 i 结尾的最长递增子序列长度，依赖左边已算好的 dp[j]