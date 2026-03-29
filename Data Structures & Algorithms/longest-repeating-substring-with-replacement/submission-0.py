class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        freqs = {}
        start = 0

        for i, char in enumerate(s):
            freqs[char] = freqs.get(char, 0) + 1
            max_freq = max(max_freq, freqs[char])

            while (i-start+1) - max_freq > k:
                freqs[s[start]] -= 1
                start += 1
            
            max_len = max(max_len, i-start+1)
        
        return max_len