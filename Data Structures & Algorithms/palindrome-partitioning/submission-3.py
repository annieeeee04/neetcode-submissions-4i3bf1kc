class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def isPalindrome(char):
            l, r = 0, len(char)-1
            while l < r:
                if char[l] != char[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i, path):
            if i >= len(s):
                out.append(path[:])
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(j+1, path)
                    path.pop()
        backtrack(0, [])
        return out