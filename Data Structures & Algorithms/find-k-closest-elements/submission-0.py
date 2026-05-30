class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for n in arr:
            heapq.heappush(minHeap, (abs(n-x), n))
        
        out = []
        for _ in range(k):
            dist, n = heapq.heappop(minHeap)
            out.append(n)

        out.sort()
        return out