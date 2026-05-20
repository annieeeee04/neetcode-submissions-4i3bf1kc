class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n,0) + 1
        
        minHeap = [(freq, v) for (v, freq) in freqs.items()]
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return [v for _, v in minHeap]