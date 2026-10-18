class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda i: i[0])
        out = []

        for i in intervals:
            if out and out[-1][1] >= i[0]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out