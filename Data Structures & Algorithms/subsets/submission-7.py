# Time: O(n · 2ⁿ), 2ⁿ subsets and O(n) for each copy
# Space: O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(i, path):
            out.append(path[:]) # O(n), append directly

            for j in range(i, len(nums)):
                path.append(nums[j]) 
                backtrack(j+1, path) # include path
                path.pop()           # exclude path
        
        backtrack(0, [])
        return out
