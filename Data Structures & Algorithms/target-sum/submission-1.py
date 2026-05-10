# Bottom-up DP
# Time: O(n*t)
# Space: O(n*t)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} # value -> ways to achieve
        cache[0] = 1

        for n in nums:
            next_cache = {}
            for total, ways in cache.items():
                next_cache[total+n] = next_cache.get(total+n, 0) + ways
                next_cache[total-n] = next_cache.get(total-n, 0) + ways
            cache = next_cache
        return cache.get(target, 0)