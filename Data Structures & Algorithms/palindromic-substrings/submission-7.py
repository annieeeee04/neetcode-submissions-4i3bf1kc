class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i,j):
            cnt = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt
        
        out = 0
        for i in range(len(s)):
            out += expand(i,i) + expand(i,i+1)
        return out