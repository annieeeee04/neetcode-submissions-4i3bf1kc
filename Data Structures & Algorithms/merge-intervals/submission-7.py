class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        out = [intervals[0]]
        for i in intervals[1:]:
            if out[-1][1] >= i[0]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out