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
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # Sort by start time
        intervals.sort(key = lambda i: i.start)

        # Min-heap of end times
        minHeap = []
        for i in intervals:
            if minHeap and minHeap[0] <= i.start:
                heapq.heapreplace(minHeap, i.end)
            else:
                heapq.heappush(minHeap, i.end)
        return len(minHeap)

