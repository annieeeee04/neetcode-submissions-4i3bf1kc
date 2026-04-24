# Time: O(k log k), k = max_speed

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = 0
        for p in piles:
            if p > max_speed:
                max_speed = p
        
        def eatTime(s):
            time = 0
            for p in piles:
                time += (p + s - 1) // s
            return time
        
        l, r = 1, max_speed
        while l < r:
            mid = (l + r) // 2
            time = eatTime(mid)
            
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l