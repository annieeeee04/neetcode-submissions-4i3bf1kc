class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l+r) // 2
            sqr = mid ** 2
            if sqr == x:
                return mid
            if sqr > x:
                r = mid - 1
            else:
                l = mid + 1
        return r