class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse = True)
        if nums[0] > target: return False

        subset = [0] * k
        def backtrack(i):
            if i == len(nums):
                return True
            
            cur = nums[i]
            for j in range(k):
                if j > 0 and subset[j] == subset[j-1]:
                    continue
                if cur + subset[j] <= target:
                    subset[j] += cur
                    if backtrack(i+1):
                        return True
                    subset[j] -= cur
            return False
        
        return backtrack(0)