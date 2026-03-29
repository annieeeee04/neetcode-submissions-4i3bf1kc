class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            while len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]