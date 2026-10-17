# Time: O(n log n)   (sorting dominates; the merge pass is O(n))
# Space: O(n)        (output list; sort is in place)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]
        path = []

        intervals.sort(key = lambda x: x[0])
        for x in intervals:
            if path and path[-1][1] >= x[0]:
                path[-1][1] = max(path[-1][1], x[1])
            else:
                path.append(x)
        return path