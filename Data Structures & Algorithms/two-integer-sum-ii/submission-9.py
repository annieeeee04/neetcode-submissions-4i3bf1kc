class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}

        for i, n in enumerate(numbers):
            if target - n in cache:
                return [cache[target-n]+1, i+1]
            
            cache[n] = i