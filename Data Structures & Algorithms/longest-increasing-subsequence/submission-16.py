# O(n^2)
# O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # dp[i] = LIS length starting at i

        for i in range(len(nums)-1, -1, -1):
            # every dp[j] with j > i is already final when you compute dp[i]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)