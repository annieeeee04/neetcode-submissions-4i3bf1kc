class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        prev = intervals[0]

        path = []
        intervals.sort(key = lambda x: x[0])
        for i in intervals:
            if path and i[0] <= path[-1][1]:
                path[-1][1] = max(i[1], path[-1][1])
            else:
                path.append(i)
        return path