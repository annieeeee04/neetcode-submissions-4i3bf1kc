class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_cur, min_cur = 0, 0
        max_sum, min_sum = float('-inf'), float('inf')

        for n in nums:
            max_cur = max(n, max_cur + n)
            max_sum = max(max_sum, max_cur)

            min_cur = min(n, min_cur + n)
            min_sum = min(min_sum, min_cur)

            total += n
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total - min_sum)