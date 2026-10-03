class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x,y in points:
            d = x**2 + y**2
            heapq.heappush(dists, (-d, [x,y]))
            if len(dists) > k:
                heapq.heappop(dists)
        
        return [p for d,p in dists]