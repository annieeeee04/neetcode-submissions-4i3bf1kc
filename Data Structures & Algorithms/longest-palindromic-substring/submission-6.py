class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        best = ''
        for i in range(len(s)):
            odd = extend(i,i)
            even = extend(i, i+1)
            best = max(even, odd, best, key = len)
        return best