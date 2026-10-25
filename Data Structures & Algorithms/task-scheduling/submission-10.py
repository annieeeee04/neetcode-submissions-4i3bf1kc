class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()

        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0:
                    queue.append((cnt, time+n))
            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
