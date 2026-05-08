# Time: O(n * target)
# Space: O(target)
# where target = sum(nums) // 2

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
         # odd total → can never split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True  # sum of 0 is always achievable (empty subset)

        for n in nums:
            # traverse RIGHT TO LEFT to avoid using same element twice
            for j in range(target, n-1, -1):
                dp[j] = dp[j] or dp[j-n]
        
        return dp[target]