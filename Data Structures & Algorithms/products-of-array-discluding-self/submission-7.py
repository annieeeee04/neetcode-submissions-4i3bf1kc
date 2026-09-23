class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        n = len(nums)
        res = [1] * n

        for i in range(n):
            res[i] *= left
            left *= nums[i]
        
        for j in range(n-1, -1, -1):
            res[j] *= right
            right *= nums[j]
        
        return res