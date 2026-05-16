class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda i: i[0])

        path = [intervals[0]]
        for i in intervals[1:]:
            prev = path[-1]
            if i[0] <= prev[1]:
                prev[1] = max(prev[1], i[1])
            else:
                path.append(i)
        return path