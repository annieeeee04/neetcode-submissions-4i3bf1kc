class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for t in tasks:
            freqs[t] = freqs.get(t,0) + 1
        
        maxHeap = [-f for f in freqs.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0
        
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
            