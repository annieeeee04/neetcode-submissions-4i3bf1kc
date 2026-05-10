# Time: O(log n)
# Space: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(n):
            return sum(int(d) ** 2 for d in str(n))
        
        slow, fast = n, sumSquares(n)
        # With OR, both conditions would need to be False to exit
        while fast != 1 and slow != fast:
            slow = sumSquares(slow)
            fast = sumSquares(sumSquares(fast))
        
        return fast == 1