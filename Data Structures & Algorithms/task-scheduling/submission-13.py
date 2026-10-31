# Time: O(T * n) worst case, T = len(tasks); 
#     loop runs once per cycle, cycles = T + idles, 
#     idles <= (maxFreq - 1) * n < T * n
#     heap ops are O(log 26) = O(1)
# Space: O(1), at most 26 distinct tasks in freqs, heap and queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        queue = deque()
        maxHeap = [-cnt for t,cnt in count.items()]
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time