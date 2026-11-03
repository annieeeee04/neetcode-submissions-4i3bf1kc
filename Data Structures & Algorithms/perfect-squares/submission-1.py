class Solution:
    def numSquares(self, n: int) -> int:
        cache = {0: 0}             
        squares = [k * k for k in range(int(n ** 0.5), 0, -1)]

        def dfs(rem):
            if rem in cache:
                return cache[rem]
            best = float('inf')
            for s in squares:
                if s <= rem:
                    best = min(best, 1 + dfs(rem - s))
            cache[rem] = best
            return best
        
        return dfs(n)