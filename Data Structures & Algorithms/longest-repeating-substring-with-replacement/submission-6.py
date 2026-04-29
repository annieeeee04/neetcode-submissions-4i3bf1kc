class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        maxFreq = 0
        l = 0
        best = 0
        for r, char in enumerate(s):
            freqs[char] = freqs.get(char,0) + 1
            maxFreq = max(maxFreq, freqs[char])
            while (r-l+1) - maxFreq > k:
                freqs[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best