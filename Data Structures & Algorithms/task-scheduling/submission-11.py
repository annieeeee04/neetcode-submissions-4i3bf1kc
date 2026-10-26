# Time: O(T * n) worst case, T = len(tasks); 
#     loop runs once per cycle, cycles = T + idles, 
#     idles <= (maxFreq - 1) * n < T * n
#     heap ops are O(log 26) = O(1)
# Space: O(1), at most 26 distinct tasks in freqs, heap and queue
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
