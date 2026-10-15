class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for n in nums:
            temp = cur
            cur = max(cur, prev+n)
            prev = temp
        return cur