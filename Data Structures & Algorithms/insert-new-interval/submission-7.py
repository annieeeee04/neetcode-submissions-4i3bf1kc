class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval: 
            return [newInterval]
        
        if not newInterval:
            return intervals
        
        intervals.append(newInterval)
        intervals.sort(key = lambda i: i[0])
        out = [intervals[0]]

        for i in intervals[1:]:
            prev = out[-1]
            if prev[1] >= i[0]:
                prev[1] = max(prev[1], i[1])
            else:
                out.append(i)
        return out