# Memoization DFS (top-down
# Time: O()
# Space: O()

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (i, total) -> number of ways
        
        def dfs(i, total):
            if i == len(nums):
                return 1 if target == total else 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (dfs(i+1, total + nums[i]) +   # add
                              dfs(i+1, total - nums[i]))     # subtract
            return dp[(i, total)]

        return dfs(0, 0)