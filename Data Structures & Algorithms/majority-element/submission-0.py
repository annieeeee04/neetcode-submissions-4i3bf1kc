class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = {}
        major = len(nums) // 2
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        for n, freq in freqs.items():
            if freq >= major:
                return n