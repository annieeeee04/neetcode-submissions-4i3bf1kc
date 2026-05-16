class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        farthest = 0
        n = len(nums)
        res = 0

        while r < n - 1:
            for i in range(l, r+1):
                farthest = max(farthest, nums[i] + i)
            l, r = r+1, farthest
            res += 1
        return res