import random
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)

        def quickSort(low, high):
            if low >= high:
                return
            p = nums[random.randint(low, high)]
            l, i, r = low, low, high
            while i <= r:
                if nums[i] < p:
                    nums[l], nums[i] = nums[i], nums[l]
                    i += 1
                    l += 1
                elif nums[i] > p:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -= 1
                else:
                    i += 1
            quickSort(low, l-1)
            quickSort(r+1, high)

        quickSort(0, len(nums)-1)
        for i, n in enumerate(nums):
            if n == target:
                return i