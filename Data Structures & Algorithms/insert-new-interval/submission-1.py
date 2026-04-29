class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval: 
            return [newInterval]
        
        if not newInterval:
            return intervals
        
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        path = []
        for x in intervals:
            if path and path[-1][1] >= x[0]:
                path[-1][1] = max(path[-1][1], x[1])
            else:
                path.append(x)
        return path