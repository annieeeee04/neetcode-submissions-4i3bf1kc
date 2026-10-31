class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap, res = [], []
        jobs = sorted(
            (enq, proc, idx) for idx, (enq, proc) in enumerate(tasks)
        )
        n = len(jobs)
        time, i = 0, 0
        res = []

        while len(res) < n:
            # no tasks waiting in line and current time is smaller than the 
            # earliest next available one
            if not minHeap and time < jobs[i][0]:
                time = jobs[i][0]
            
            # while there's a task being processed, but some others are ready
            # to be preocessed as well, add them in line(earliest -> latest)
            while i < n and jobs[i][0] <= time:
                heapq.heappush(minHeap, (jobs[i][1], jobs[i][2]))
                i += 1
            
            # after appending all waiting tasks, process the current one
            # and update the time
            proc, idx = heapq.heappop(minHeap)
            time += proc
            res.append(idx)
        
        return res