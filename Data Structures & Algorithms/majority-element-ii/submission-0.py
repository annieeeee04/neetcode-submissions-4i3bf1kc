class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        out = []
        for n, freq in freqs.items():
            if freq > threshold:
                out.append(n)
        return out