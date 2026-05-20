class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        out = [1] * len(nums)

        for i, n in enumerate(nums):
            out[i] *= left
            left *= n
        
        for i in range(len(nums)-1, -1, -1):
            out[i] *= right
            right *= nums[i]
        
        return out