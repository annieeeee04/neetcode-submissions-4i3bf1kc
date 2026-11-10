class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        up, down = 1, 1
        n = len(arr)

        if n < 2:
            return n

        for i in range(1, n):
            if arr[i] - arr[i-1] < 0:
                up = down + 1
                down = 1
            elif arr[i] - arr[i-1] > 0:
                down = up + 1
                up = 1
            else:
                up = 1
                down = 1
            best = max(up, down, best)
        
        return best