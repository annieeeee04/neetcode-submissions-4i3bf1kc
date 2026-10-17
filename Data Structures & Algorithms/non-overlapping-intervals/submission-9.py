class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num = 0
        intervals.sort(key = lambda i: i[0])

        prev = intervals[0]
        start, end = prev[0], prev[1]
        for i in intervals[1:]:
            if i[0] < end:
                num += 1
                end = min(end, i[1])
            else:
                end = i[1]
        return num