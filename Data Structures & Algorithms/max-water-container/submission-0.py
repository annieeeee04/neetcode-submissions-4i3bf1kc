class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        max_area = 0
        l, r = 0, len(heights)-1
        while l <= r:
            lHeight = heights[l]
            rHeight = heights[r]
            width = r - l
            area = min(lHeight, rHeight) * width
            if lHeight < rHeight:
                l += 1
            else:
                r -= 1

            max_area = max(area, max_area)
        
        return max_area
