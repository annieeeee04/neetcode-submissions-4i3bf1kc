class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i, n in enumerate(nums):
            if target - n in record:
                return [record[target-n], i]
            else:
                record[n] = i
        