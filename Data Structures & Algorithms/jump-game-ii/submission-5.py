class Solution:
    def jump(self, nums: List[int]) -> int:
        rightMost = 0
        l, r = 0, 0
        rest = 0

        while r < len(nums)-1:
            for i in range(l, r+1):
                rightMost = max(rightMost, i+nums[i])
            l, r = r+1, rightMost
            rest += 1
        return rest