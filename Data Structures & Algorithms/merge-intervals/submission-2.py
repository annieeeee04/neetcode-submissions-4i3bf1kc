class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        path = []
        intervals.sort(key = lambda i : i[0])
        for i in intervals:
            if path and path[-1][1] >= i[0]:
                path[-1][1] = max(path[-1][1], i[1])
            else:
                path.append(i)
        return path
            