# Time: O(n), technically O(n logk), k = distinct elemets = 3
# Space: O(n) for the output, O(1) for the heap
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')):
            if cnt > 0:
                maxHeap.append((-cnt, ch))
        heapq.heapify(maxHeap)
        res = []

        while maxHeap:
            cnt, ch = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                if not maxHeap:
                    break
                cnt2, ch2 = heapq.heappop(maxHeap)
                res.append(ch2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(maxHeap, (cnt2, ch2))
                heapq.heappush(maxHeap, (cnt, ch))
            else:
                res.append(ch)
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, (cnt, ch))
        
        return ''.join(res)