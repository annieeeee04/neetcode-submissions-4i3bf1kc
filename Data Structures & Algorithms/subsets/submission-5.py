class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(i, path):
            out.append(path[:])

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
        
        backtrack(0, [])
        return out
