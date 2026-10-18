# Time: O(n)
# Space: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, i, n = [], 0, len(intervals)
        # entirely before
        while i < n and intervals[i][1] < newInterval[0]:       
            res.append(intervals[i]); i += 1
        # overlapping: absorb
        while i < n and intervals[i][0] <= newInterval[1]:      
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)
        
        # entirely after
        res.extend(intervals[i:])                               
        return res