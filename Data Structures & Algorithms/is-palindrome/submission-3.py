class Solution:
    def isPalindrome(self, s: str) -> bool:
        path = []

        for char in s:
            if char.isalnum():
                path.append(char.lower())
        
        return path == path[::-1]