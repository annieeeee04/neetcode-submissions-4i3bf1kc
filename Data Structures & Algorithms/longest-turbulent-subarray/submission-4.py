class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up, down = 1, 1
        best = 1
        n = len(arr)
        if n < 2:
            return n
            
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                up = down + 1
                down = 1
            elif arr[i-1] < arr[i]:
                down = up + 1
                up = 1
            else:
                down = 1
                up = 1
            best = max(best, up, down)
            
        return best