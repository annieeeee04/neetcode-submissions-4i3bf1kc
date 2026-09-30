class Solution:
    def isPalindrome(self, s: str) -> bool:
        record = ''
        for char in s:
            if char.isalnum():
                record += char.lower()
        
        l, r = 0, len(record) - 1
        while l < r:
            if record[l] != record[r]:
                return False
            l += 1
            r -= 1
        return True
