class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def backtrack(i, path):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()

        backtrack(0, [])
        return res