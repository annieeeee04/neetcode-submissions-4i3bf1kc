class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        cur_end = intervals[0][1]
        num = 0

        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval[0], interval[1]
            if start < cur_end:
                num += 1
            else:
                cur_end = end
        return num