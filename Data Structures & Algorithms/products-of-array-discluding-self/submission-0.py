class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)

        for i in range(1,len(nums)):
            leftProduct[i] = nums[i-1] * leftProduct[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            rightProduct[j] = nums[j+1] * rightProduct[j+1]
        
        out = [1] * len(nums)
        for i in range(len(nums)):
            out[i] = leftProduct[i] * rightProduct[i]
        
        return out