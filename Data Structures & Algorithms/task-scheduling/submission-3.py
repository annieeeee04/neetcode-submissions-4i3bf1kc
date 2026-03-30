class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count task frequencies and initialize max-heap 
        # (negative for min-heap logic)
        freqs = {}
        for t in tasks:
            freqs[t] = freqs.get(t, 0) + 1
        
        max_heap = [-f for f in freqs.values()]
        heapq.heapify(max_heap)
        # Queue tracks [remaining_count, available_time] for tasks in cooling
        queue = deque()

        time = 0
        while max_heap or queue:
            time += 1
            if max_heap:
                # Process most frequent task; if count remains, move to cooling queue
                cnt = 1 + heapq.heappop(max_heap)
                # if there's still some same tasks left, add to the queue
                if cnt:
                    queue.append([cnt, time + n])
            # If cooling period ends for the earliest task, move it back to heap
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time