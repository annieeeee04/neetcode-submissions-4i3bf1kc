class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = float('-inf')

        for n in nums:
            cur = max(n, cur + n)
            best = max(cur, best)
        
        return best
