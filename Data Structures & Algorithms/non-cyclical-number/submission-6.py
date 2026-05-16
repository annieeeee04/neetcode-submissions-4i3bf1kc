class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        seen = set()
        while total != 1:
            total = 0
            for char in str(n):
                total += int(char) ** 2
            if total in seen:
                return False
            else:
                seen.add(total)
            n = total
        return True
            
