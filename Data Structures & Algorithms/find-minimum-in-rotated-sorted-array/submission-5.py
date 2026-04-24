# Time: O(log n)
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1 # Min must be to the right
            else:
                r = mid # mid could be the min
        return nums[l]