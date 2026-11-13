class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, i, hi = 0, 0, len(nums)-1
        while i <= hi:
            if nums[i] == 0:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            else:
                i += 1
        