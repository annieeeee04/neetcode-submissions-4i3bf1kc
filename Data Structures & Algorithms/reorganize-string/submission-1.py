# Time: O(n log k), k = distinct chars (k <= 26, so effectively O(n))
# Space: O(k) for the heap, plus O(n) for the output
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-c, ch) for ch, c in count.items()] 
        heapq.heapify(maxHeap) 
        res = []
        prev = None 

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            c, ch = heapq.heappop(maxHeap)
            res.append(ch)
            c += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if c < 0:
                prev = (c, ch)

        return ''.join(res)