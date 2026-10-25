class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-c, ch) for ch, c in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        res = []

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            c, ch = heapq.heappop(maxHeap)
            c += 1
            res.append(ch)

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if c < 0:
                prev = (c, ch)
        
        return ''.join(res)