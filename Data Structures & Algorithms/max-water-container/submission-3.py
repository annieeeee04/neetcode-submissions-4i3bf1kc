class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        maxarea = 0

        l, r = 0, len(heights) - 1
        while l <= r:
            lHeight = heights[l]
            rHeight = heights[r]
            width = r - l 
            area = width * min(lHeight, rHeight)
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1
            maxarea = max(maxarea, area)

        return maxarea