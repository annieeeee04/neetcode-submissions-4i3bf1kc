# Time: O(log n), halves the search space each iteration
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # mid is still in the high run (before the rotation
            # point) -> min is strictly to the right, mid can't be it
            if nums[mid] > nums[r]:
                l = mid + 1
            # mid is already in the low run (or window is sorted)
            # -> min is at mid or to its left, keep mid as candidate
            else:
                r = mid
        # l == r here, converged on the minimum
        return nums[l]