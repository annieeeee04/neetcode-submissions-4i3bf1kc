class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_cur, max_cur = 0, 0
        maxSum = float('-inf')
        minSum = float('inf')

        total = 0
        for n in nums:
            max_cur = max(max_cur + n, n)
            maxSum = max(maxSum, max_cur)

            min_cur = min(min_cur + n, n)
            minSum = min(minSum, min_cur)

            total += n
        
        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)