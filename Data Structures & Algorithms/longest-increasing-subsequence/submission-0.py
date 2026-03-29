# DP
# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], cache[j]+1)
        return max(cache)
