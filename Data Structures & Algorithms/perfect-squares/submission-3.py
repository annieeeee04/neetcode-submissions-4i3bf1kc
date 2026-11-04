class Solution:
    def numSquares(self, n: int) -> int:
        cache = {0: 0}             
        squares = [k * k for k in range(int(n ** 0.5), 0, -1)]

        def dfs(i):
            if i in cache:
                return cache[i]

            best = float('inf')
            for s in squares:
                if i >= s:
                    best = min(best, dfs(i-s) + 1)
            cache[i] = best
            return cache[i]
                    
        return dfs(n)