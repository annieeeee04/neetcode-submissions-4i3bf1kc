class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            first = - heapq.heappop(heap)
            second = - heapq.heappop(heap) if len(heap) > 0 else 0
            left = first - second
            heapq.heappush(heap, -left)
        if len(heap) == 0:
            return 0
        else:
            return - heap[0]