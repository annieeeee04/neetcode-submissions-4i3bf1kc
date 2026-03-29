class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                lKey = nums[l]
                rKey = nums[r]
                s = lKey + rKey + n
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return out