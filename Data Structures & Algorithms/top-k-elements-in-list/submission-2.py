class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        heap = []
        for n, cnt in freqs.items():
            heapq.heappush(heap, [cnt, n])
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for cnt, n in heap]