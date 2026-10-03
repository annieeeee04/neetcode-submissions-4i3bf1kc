class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                width = i - idx
                # calculate the area of those tall bars
                # the lower ones ahead cannot be included anyways
                maxArea = max(maxArea, width * height)
                # since the popped bar is taller, the start idx
                # should be moved one step earlier to include that
                # as when forming the rectangle in a monotonic 
                # increasing stack, that taller bar can absolute
                # be taller then the latter on in the stack, and so 
                # can be included in forming the rectangle
                start = idx
            # but record the future lower ones with their index
            stack.append([start, h])
        
        # since tit monotonic increasing stack
        # the current visiting height can always make a rectangle 
        # with length (len(stack) - i)
        for (i, h) in stack:
            w = len(heights) - i
            maxArea = max(maxArea, w * h)
        return maxArea