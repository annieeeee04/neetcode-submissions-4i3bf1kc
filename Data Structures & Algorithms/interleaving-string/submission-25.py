class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for r in range(1, m+1):
            for c in range(1, n+1):
                if dp[r-1][c] and s1[r-1] == s3[r+c-1]:
                    dp[r][c] = True
                elif dp[r][c-1] and s2[c-1] == s3[r+c-1]:
                    dp[r][c] = True
        return dp[m][n]