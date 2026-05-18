class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        rest = self.permute(nums[1:])

        out = []
        for record in rest:
            for i in range(len(record)+1):
                copy = record.copy()
                copy.insert(i, nums[0])
                out.append(copy)
        return out