class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]] 
        
        perms = self.permuteUnique(nums[1:])
        first = nums[0]
        out = []
        seen = set()

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, first)
                key = tuple(p_copy)
                if key in seen:
                    continue
                seen.add(key)
                out.append(p_copy)
        
        return out