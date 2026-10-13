# Time: O(n × S), n = len(nums), S = sum of all elements in nums
# Total dimension: total can range from -S to +S -> O(S)
# Index dimension: i ranges from 0 to n, giving -> O(n)

# Memoization: Each unique (i, total) pair is computed only once, 
# so we have O(n × S) total states
# Space: O(n × S)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        out = 0
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in cache:
                return cache[(i,total)]
            
            cache[(i, total)] = (dfs(i+1, total + nums[i]) + 
                                 dfs(i+1, total - nums[i]))
            return cache[(i, total)]
        
        return dfs(0, 0)