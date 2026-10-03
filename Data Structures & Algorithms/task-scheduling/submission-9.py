from collections import deque
# Time: O(T · n) worst case, T = len(tasks)
#   (heap ops are O(1) since ≤26 distinct tasks; the loop count
#   itself — the answer — can blow up due to idle slots)
# Space: O(n), queue holds at most n+1 pending tasks at once
#   (freqs/heap are O(1), bounded by the 26-letter alphabet)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        freqs = {}

        for t in tasks:
            freqs[t] = freqs.get(t,0) + 1
        max_heap = [-f for f in freqs.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while queue or max_heap:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
