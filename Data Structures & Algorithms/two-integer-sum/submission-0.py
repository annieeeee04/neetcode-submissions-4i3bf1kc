class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        path = {}

        for i, n in enumerate(nums):
            remain = target - n
            if remain in path:
                return [path[remain], i]
            else:
                path[n] = i
