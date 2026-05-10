class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        out = 1
        if n < 0:
            for _ in range(-n):
                out *= x
            return float(1 / out)
        else:
            for _ in range(n):
                out *= x
            return float(out)