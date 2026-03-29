class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]
        for n, freq in freqs.items():
            buckets[freq].append(n)
        
        res = []
        for f in range(len(buckets)-1,0, -1):
            for n in buckets[f]:
                res.append(n)
                if len(res) == k:
                    return res
                    