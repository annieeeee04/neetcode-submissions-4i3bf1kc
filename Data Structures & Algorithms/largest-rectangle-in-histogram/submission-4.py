class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, prev = stack.pop()
                maxArea = max(maxArea, (i-idx)*prev)
                start = idx
            stack.append((start,h))
        
        n = len(heights)
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, (n-i) * h)
        return maxArea