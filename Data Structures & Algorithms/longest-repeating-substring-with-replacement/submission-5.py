class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        best = 0
        maxFreq = 0
        l = 0

        for r, char in enumerate(s):
            freqs[char] = freqs.get(char, 0) + 1
            maxFreq = max(maxFreq, freqs[char])
            while r-l+1 - maxFreq > k:
                freqs[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        
        return best