"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Time: O(n log n)
# Space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        minHeap = []
        for i in intervals:
            if minHeap and i.start >= minHeap[0]:
                heapq.heappop(minHeap) # free the earliest-ending room
            heapq.heappush(minHeap, i.end)

        return len(minHeap)