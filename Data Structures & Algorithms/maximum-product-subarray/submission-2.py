# Time: O(N)
# Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        best = nums[0]
        
        for n in nums[1:]:
            candidates = [n, cur_max*n, cur_min*n]

            # all 3 candidates for new max/min:
            # 1. n itself          → start fresh from here
            # 2. curMax * n        → extend current max streak
            # 3. curMin * n        → negative × negative = positive!
            cur_max = max(candidates)
            cur_min = min(candidates)
            best = max(cur_max, best)
        
        return best