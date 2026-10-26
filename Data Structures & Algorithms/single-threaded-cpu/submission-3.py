class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        jobs = sorted((enq, proc, idx) for idx, (enq, proc) in enumerate(tasks))
        minHeap = []
        res = []
        time = 0
        i = 0
        n = len(jobs)

        while len(res) < n:
            if not minHeap and time < jobs[i][0]:
                time = jobs[i][0]
            
            while i < n and time >= jobs[i][0]:
                heapq.heappush(minHeap, (jobs[i][1], jobs[i][2]))
                i += 1
            
            proc, idx = heapq.heappop(minHeap)
            res.append(idx)
            time += proc
        
        return res