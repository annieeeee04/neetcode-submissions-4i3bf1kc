class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shipTime(cap):
            cur = 0
            d = 1
            for w in weights:
                if w + cur > cap:
                    cur = 0
                    d += 1
                cur += w
            return d

        l, r = max(weights), sum(weights)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            d = shipTime(mid)
            if d <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans