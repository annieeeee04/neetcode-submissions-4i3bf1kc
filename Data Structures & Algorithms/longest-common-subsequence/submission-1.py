class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # the first column & row are the base case, 
        # containing all zeros
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                # if letters match, use 1 + the left upper corner
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                # otherwise take the max between the 
                # upper one and the left one
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[n][m]