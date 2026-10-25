class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        jobs = sorted(
            (enq, proc, i) for i, (enq, proc) in enumerate(tasks)
        )
        n = len(jobs)
        # heap holds (processingTime, index) of available tasks
        heap, res = [], []  
        time = 0 # current CPU time     
        i = 0 # next processed job                  

        while len(res) < n:
            if not heap and time < jobs[i][0]:
                time = jobs[i][0]
            
            while i < n and jobs[i][0] <= time:
                heapq.heappush(heap, [jobs[i][1], jobs[i][2]])
                i += 1
            
            proc, idx = heapq.heappop(heap)
            time += proc
            res.append(idx)

        return res