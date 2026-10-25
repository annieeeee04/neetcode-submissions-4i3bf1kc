class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 0
        farthest = 0
        jump = 0

        while end < len(nums) - 1:
            for i in range(start, end+1):
                farthest = max(farthest, i + nums[i])
            start, end = end+1, farthest
            jump += 1
        return jump