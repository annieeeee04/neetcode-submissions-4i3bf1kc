class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(l,r):
            if (l,r) in memo:
                return memo[(l,r)]

            if l == r:
                return piles[l]

            res = max(piles[l] - dfs(l+1,r), piles[r] - dfs(l,r-1))
            memo[(l,r)] = res
            return memo[(l,r)]
            
        return dfs(0, len(piles)-1) > 0