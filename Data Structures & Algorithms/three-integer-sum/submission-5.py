class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                s = n + nums[l] + nums[r]
                if s == 0:
                    out.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return out