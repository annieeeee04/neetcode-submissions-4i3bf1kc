class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        res = []
        maxHeap = [(-cnt, ch) for (ch, cnt) in count.items()]
        heapq.heapify(maxHeap)
        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ''
            
            cnt, ch = heapq.heappop(maxHeap)
            res.append(ch)
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt < 0:
                prev = (cnt, ch)
        return ''.join(res)