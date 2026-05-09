"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Time: O(nlogn)
# Space: O(n)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        
        intervals.sort(key = lambda i : i.start)

        prev = intervals[0]
        for i in intervals[1:]:
            if i.start < prev.end:
                return False
            prev = i
        
        return True