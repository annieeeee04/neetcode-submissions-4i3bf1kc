class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0:1}
        def dfs(remain):
            if remain in cache:
                return cache[remain]
            
            total = 0
            for x in nums:
                if x <= remain:
                    total += dfs(remain - x)
            cache[remain] = total
            return total
        
        return dfs(target)