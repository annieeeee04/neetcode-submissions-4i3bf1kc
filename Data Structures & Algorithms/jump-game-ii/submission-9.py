class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        l, r = 0, 0

        num = 0
        while r < len(nums) - 1:
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l, r = r+1, farthest
            num += 1
        return num