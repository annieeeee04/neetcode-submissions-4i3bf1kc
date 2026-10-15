class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        best = ''
        for i in range(len(s)):
            even = expand(i,i)
            odd = expand(i, i+1)
            best = max(best, even, odd, key = len)
        return best