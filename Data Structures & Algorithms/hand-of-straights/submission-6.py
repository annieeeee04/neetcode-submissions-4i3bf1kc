class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        graph = {}
        for n in hand:
            graph[n] = graph.get(n,0) + 1
        
        minHeap = list(graph.keys())
        heapq.heapify(minHeap)
        while minHeap:
            start = minHeap[0]  # peek, don't pop yet
            for i in range(groupSize):
                if graph.get(start + i, 0) == 0:
                    return False
                graph[start + i] -= 1
                if graph[start + i] == 0:
                    heapq.heappop(minHeap)
        return True