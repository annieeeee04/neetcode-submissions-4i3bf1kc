class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        n = len(piles)

        def dfs(l,r):
            if l == r:
                return piles[l]
            
            if (l,r) in cache:
                return cache[(l,r)]

            res = max(piles[l] + dfs(l+1,r), piles[r-1] + dfs(l, r-1))
            cache[(l,r)] = res
            return cache[(l,r)]
        
        return dfs(0, n-1) > 0