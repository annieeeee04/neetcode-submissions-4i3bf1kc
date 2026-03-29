class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            # Push negative to simulate Max-Heap
            heapq.heappush(heap, [-nums[i], i])

            # Once we've reached at least k elements
            if i >= k - 1:
                # Clean up the top of the heap if it's outside the window
                # A window ending at i and having size k starts at i - k + 1
                # So any index <= i - k is invalid
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                
                # The top is now guaranteed to be the max within [i-k+1, i]
                res.append(-heap[0][0])
        return res