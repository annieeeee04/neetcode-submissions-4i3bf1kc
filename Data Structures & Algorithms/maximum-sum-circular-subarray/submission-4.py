class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_cur, min_cur = 0, 0
        maxSum, minSum = float('-inf'), float('inf')
        total = 0

        for n in nums:
            max_cur = max(n, max_cur + n)
            maxSum = max(maxSum, max_cur)

            min_cur = min(n, min_cur + n)
            minSum = min(minSum, min_cur)

            total += n
        
        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)