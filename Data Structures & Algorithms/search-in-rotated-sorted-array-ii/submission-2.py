# Time: O(log n) on average, O(n) worst case (e.g. mostly equal values)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            
            # can't tell which half is sorted
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False