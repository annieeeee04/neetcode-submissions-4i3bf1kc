class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eatTime(v):
            time = 0
            for p in piles:
                time += (p+v-1) // v
            return time
        
        while l < r:
            mid = (l+r) // 2
            time = eatTime(mid)
            if time <= h:
                r = mid 
            else:
                l = mid + 1
        return l