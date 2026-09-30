class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        maxFreq = 0
        best = 0
        start = 0

        for i, char in enumerate(s):
            freqs[char] = freqs.get(char,0) + 1
            maxFreq = max(maxFreq, freqs[char])
            while (i-start+1) - maxFreq > k:
                freqs[s[start]] -= 1
                start += 1
            best = max(best, (i-start+1))
        return best