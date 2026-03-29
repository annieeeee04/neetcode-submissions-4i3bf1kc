# Time: O(log(max(p)) * p)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = 0
        n = len(piles)
        for p in piles:
            if p > max_speed:
                max_speed = p
        
        def eatTime(speed):
            time = 0
            for p in piles:
                time += (p+speed-1) // speed
            return time

        lo, hi = 1, max_speed
        while lo < hi:
            mid = (lo + hi) // 2
            t = eatTime(mid)

            if t <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo