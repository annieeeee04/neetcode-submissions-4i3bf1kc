class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[0])
        prev = intervals[0]
        num = 0
        for i in intervals[1:]:
            if prev[1] > i[0]:
                num += 1
                prev[1] = min(prev[1], i[1])
            else:
                prev = i
        return num