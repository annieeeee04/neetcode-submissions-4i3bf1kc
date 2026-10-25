# Time: O(n)
# Space: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max([t[2] for t in trips])
        diff = [0] * (n+1)
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        
        cur = 0
        for i in range(n+1):
            cur += diff[i]
            if cur > capacity:
                return False
        return True