class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            heapq.heappush(minHeap, (-dist, p))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [p for _, p in minHeap]