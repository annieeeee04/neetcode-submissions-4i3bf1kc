class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = set()
        cur = 0
        max_len = 0
        for i, key in enumerate(s):
            while key in seen:
                seen.remove(s[start])
                start += 1
            
            seen.add(key)
            max_len = max(i - start + 1, max_len)
        
        return max_len