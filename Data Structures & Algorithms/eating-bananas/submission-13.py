class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatTime(v):
            time = 0
            for p in piles:
                time += (p + v - 1) // v
            return time
        
        l, r = 1, max(piles)
        best = float('inf')
        while l <= r:
            mid = (l+r) // 2
            t = eatTime(mid)
            if t <= h:
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        return best