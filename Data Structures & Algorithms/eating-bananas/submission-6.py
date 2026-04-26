class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatTime(s):
            total = 0
            for p in piles:
                total += (p+s-1) // s
            return total
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            t = eatTime(mid)
            if t <= h:
                r = mid 
            else:
                l = mid + 1
        return l