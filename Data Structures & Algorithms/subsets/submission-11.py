class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(i, path):
            if i >= len(nums):
                out.append(path[:])
                return
            
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
            backtrack(i+1, path)
        
        backtrack(0, [])
        return out