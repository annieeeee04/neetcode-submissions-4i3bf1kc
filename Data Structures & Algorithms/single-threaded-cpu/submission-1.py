class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        minHeap = [] # [proc, idx]
        jobs = sorted(
            (enq, proc, i) for i, (enq, proc) in enumerate(tasks))
        time = 0 # current CPU time
        i = 0 # next processed job idx
        n = len(jobs)

        while len(res) < n:
            if not minHeap and jobs[i][0] > time:
                time = jobs[i][0]
            
            while i < n and jobs[i][0] <= time:
                heapq.heappush(minHeap, [jobs[i][1], jobs[i][2]])
                i += 1
            
            proc, idx = heapq.heappop(minHeap)
            time += proc
            res.append(idx)
        
        return res