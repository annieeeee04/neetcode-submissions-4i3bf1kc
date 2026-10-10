class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        def expend(l,r):
            nonlocal cnt
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
        
        for i in range(len(s)):
            expend(i,i)
            expend(i,i+1)
        return cnt