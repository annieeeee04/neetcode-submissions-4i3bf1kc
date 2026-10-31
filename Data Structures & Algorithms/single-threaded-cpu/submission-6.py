# Time: O(n log n)
# Space: O(n)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # minHeap holds (proc, idx) of tasks that have arrived
        minHeap, res = [], []
        # sort by enqueue time, keep original idx                        
        jobs = sorted(
            (enq, proc, idx) for idx, (enq, proc) in enumerate(tasks)   
        )
        n = len(jobs)
        # time = current CPU time, i = next job not yet in the heap
        time, i = 0, 0                                

        # stop when every task has been processed
        while len(res) < n:                           
            # CPU is idle: nothing is waiting and the next task hasn't arrived,
            # so jump the clock straight to its arrival time
            if not minHeap and time < jobs[i][0]:
                time = jobs[i][0]

            # push every task that has arrived by now (enqueue time <= time);
            # the list is sorted, so stop at the first one that hasn't arrived
            while i < n and jobs[i][0] <= time:
                heapq.heappush(minHeap, (jobs[i][1], jobs[i][2]))
                i += 1

            # run the waiting task with the shortest processing time 
            # (ties: smallest idx)
            # to completion, then advance the clock
            proc, idx = heapq.heappop(minHeap)
            time += proc
            res.append(idx)

        return res

# 中文：按到达时间排序，用最小堆（处理时间，原下标）维护已到达的任务；堆空就把时间跳到下一个任务的到达时间；只把 enq <= time 的任务入堆；循环条件是还有任务没处理完（len(res) < n）。