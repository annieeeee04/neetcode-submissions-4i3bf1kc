class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        def robLinear(nums):
            prev, cur = 0, 0
            for i in range(len(nums)):
                temp = cur
                cur = max(prev + nums[i], cur)
                prev = temp
            return cur
        
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))