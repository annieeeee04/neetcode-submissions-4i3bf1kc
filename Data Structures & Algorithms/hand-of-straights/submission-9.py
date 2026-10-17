class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        graph = {}
        for n in hand:
            graph[n] = graph.get(n,0) + 1
        minHeap = list(graph.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]
            for n in range(first, first + groupSize):
                if n not in graph:
                    return False
                graph[n] -= 1
                if graph[n] == 0:
                    if n != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True