class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        queue = deque() # [-cnt, time]

        # first deal with the maxHeap,
        # if there's nothing then go to the queue
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # if there's still task left, 
                    # add it to the queue and wait at least 'n' period
                    # to deal with it
                    queue.append([cnt, time+n])
            # if there's task in the queue and the wait time reaches 0
            # add it back to the maxHeap -> activate again
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time