# Time: O(n · P)
# Space: O(n)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        path, out = [], []

        def backtrack():
            if len(path) == len(nums):
                out.append(path[:])
            
            for x in count:
                if count[x] > 0:
                    count[x] -= 1
                    path.append(x)
                    backtrack()
                    path.pop()
                    count[x] += 1
        backtrack()
        return out