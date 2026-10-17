class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num = 0
        intervals.sort(key = lambda i: i[0])

        prev = intervals[0]
        start, end = prev[0], prev[1]
        for i in intervals[1:]:
            # overlap: remove the one that ends later
            if i[0] < end:
                num += 1
                end = min(end, i[1])
            # no overlap: move on to this interval
            else:
                end = i[1]
        return num