class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        minHeap = hand
        heapq.heapify(minHeap)
        graph = {}
        for n in hand:
            graph[n] = graph.get(n,0) + 1
        
        while minHeap:
            start = heapq.heappop(minHeap)
            graph[start] -= 1
            if graph[start] == 0:
                del graph[start]

            for _ in range(groupSize-1):
                if start+1 in graph:
                    minHeap.remove(start+1)
                    heapq.heapify(minHeap)
                    graph[start+1] -= 1
                    if graph[start+1] == 0:
                        del graph[start+1]
                    start += 1
                else:
                    return False
        return True