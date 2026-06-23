class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        k = 0
        for i in range(len(nums)):
            n = nums[i]
            if n != val:
                nums[start] = n
                start += 1

        k = start
        for j in range(start, len(nums)):
            nums[j] = '_'
        
        return k