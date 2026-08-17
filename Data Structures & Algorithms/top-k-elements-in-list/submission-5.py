# Time: O(n log k)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []

        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n,0) + 1

        for n, freq in freqs.items():
            heapq.heappush(minHeap, (freq, n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [n for (freq, n) in minHeap]