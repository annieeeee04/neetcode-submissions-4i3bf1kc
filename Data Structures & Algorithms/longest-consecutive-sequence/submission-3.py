# Time: O(n)
# Space: O(1)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        cur = 0
        record = set(nums)

        for n in record:
            if n-1 in record:
                continue
            
            while n in record:
                cur += 1
                n += 1
            best = max(best, cur)
            cur = 0
        
        return best