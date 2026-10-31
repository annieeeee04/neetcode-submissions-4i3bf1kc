class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        jobs = sorted(
            (enq, proc,idx) for idx, (enq, proc) in enumerate(tasks)
        )
        heap, res = [], []  
        n = len(jobs)
        i = 0

        time = 0
        while len(res) < n:
            if not heap and time < jobs[i][0]:
                time = jobs[i][0]
            while i < n and time >= jobs[i][0]:
                heapq.heappush(heap, (jobs[i][1], jobs[i][2]))
                i += 1
            
            proc, idx = heapq.heappop(heap)
            res.append(idx)
            time += proc
        
        return res