class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif val < target:
                l += 1
            else:
                r -= 1
        return -1