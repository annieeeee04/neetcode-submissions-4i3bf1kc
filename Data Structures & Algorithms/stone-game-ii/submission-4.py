class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        n = len(piles)

        def dfs(i, m):
            if (i, m) in cache:
                return cache[(i,m)]
            if i == n:
                return 0
            
            best = float('-inf')
            stones = 0
            for x in range(1, min(2*m, n-i) + 1):
                stones += piles[i+x-1]
                oppo = dfs(i+x, max(m, x))
                best = max(best, stones - oppo)
                cache[(i,m)] = best
            return cache[(i,m)]
        
        max_diff = dfs(0,1)
        return (sum(piles) + max_diff) // 2
