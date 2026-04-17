class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = len(hand)
        # if the size doesn't fit, return False immediately
        if m % groupSize != 0: return False

        minHeap = []
        graph = {}
        for h in hand:
            graph[h] = graph.get(h, 0) + 1
        
        minHeap = list(graph.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start, start+groupSize):
                if i not in graph:
                    return False
                graph[i] -= 1
                if graph[i] == 0:
                    del graph[i]
                    heapq.heappop(minHeap)
        return True