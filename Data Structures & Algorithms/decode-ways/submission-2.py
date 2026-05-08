class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1                        # empty string base case
        dp[1] = 0 if s[0] == '0' else 1  # single digit base case

        for i in range(2, n + 1):
            one_digit = int(s[i-1])        # e.g. s[2] for i=3
            two_digits = int(s[i-2:i])     # e.g. s[1:3] for i=3

            if one_digit >= 1:             # single digit valid (not '0')
                dp[i] += dp[i-1]

            if 10 <= two_digits <= 26:     # two digits valid
                dp[i] += dp[i-2]

        return dp[n]