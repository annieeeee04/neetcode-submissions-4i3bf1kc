class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        if len(nums) <= 1:
            return [nums]
        
        rest = self.permute(nums[1:])
        for char in rest:
            for i in range(len(char) + 1):
                copy = char.copy()
                copy.insert(i, nums[0])
                out.append(copy)
        return out
            