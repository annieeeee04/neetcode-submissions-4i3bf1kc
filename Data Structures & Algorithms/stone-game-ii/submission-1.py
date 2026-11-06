class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def dfs(i, m):
            if (i,m) in memo:
                return memo[(i,m)]
            
            if i == n:
                return 0
            
            best = float("-inf")
            stones = 0
            for x in range(1, min(2 * m, n - i) + 1):
                stones += piles[i + x - 1]
                opponent_difference = dfs(i + x, max(m, x))
                best = max(best, stones - opponent_difference)
            memo[(i,m)] = best
            
            return memo[(i,m)]
        
        difference = dfs(0, 1)
        return (sum(piles) + difference) // 2