# Time: O(n)
# Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l+1, r+1]
            if cur < target:
                l += 1
            if cur > target:
                r -= 1
        