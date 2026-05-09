class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def robLinear(nums):
            prev = 0
            cur = 0
            for n in nums:
                temp = cur
                cur = max(n+prev, cur)
                prev = temp
            return cur
        
        return max(robLinear(nums[:-1]), robLinear(nums[1:]))