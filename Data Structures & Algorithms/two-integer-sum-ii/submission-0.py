class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            lKey = numbers[l]
            rKey = numbers[r]
            cur = lKey + rKey
            if cur == target:
                return [l+1,r+1]
            if cur < target:
                l += 1
            if cur > target:
                r -= 1
        
