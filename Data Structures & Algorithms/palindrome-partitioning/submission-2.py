class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(char):
            l, r = 0, len(char)-1
            while l <= r:
                if char[l] != char[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res =[]
        def backtrack(i, path):
            if i >= len(s):
                res.append(path[:])
                return
            
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if isPalindrome(substring):
                    # We only enter here if the left piece is valid
                    path.append(substring)     # 1. Make a choice (cut here)
                    backtrack(j + 1, path)     # 2. Explore (cut the rest)
                    path.pop()                 # 3. Undo choice (backtrack)
        
        backtrack(0, [])
        return res