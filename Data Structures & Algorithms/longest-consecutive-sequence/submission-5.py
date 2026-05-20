class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = set(nums)
        cur = 0
        best = 0
        for n in nums:
            while n-1 in record:
                n = n-1

            while n in record:
                n = n+1
                cur += 1
            
            best = max(best, cur)
            cur = 0
        
        return best