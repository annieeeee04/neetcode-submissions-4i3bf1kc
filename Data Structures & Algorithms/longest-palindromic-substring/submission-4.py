# Time: O(n²), 2n-1 centers, each expansion up to O(n)
# Space: O(1) extra, apart from the returned substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        best = ''
        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > len(best):
                best = p1

            p2 = expand(i, i+1)
            if len(p2) > len(best):
                best = p2
        
        return best