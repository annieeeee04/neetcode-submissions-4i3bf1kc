class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_freq = 0
        max_len = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            freqs[c] = freqs.get(c, 0) + 1
            max_freq = max(max_freq, freqs[c])

            if (r-l+1) - max_freq > k:
                freqs[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)

        return max_len