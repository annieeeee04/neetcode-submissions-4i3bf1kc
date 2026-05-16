class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda i: i[0])

        out = 0
        prevEnd = intervals[0][1]
        for i in intervals[1:]:
            start, end = i[0], i[1]
            if start < prevEnd:
                out += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return out