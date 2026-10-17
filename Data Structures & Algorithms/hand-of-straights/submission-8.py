class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        graph = {}
        for n in hand:
            graph[n] = graph.get(n, 0) + 1
        
        minHeap = list(graph.keys())
        heapq.heapify(minHeap)

        while minHeap:
            n = minHeap[0]
            for i in range(n, n + groupSize):
                if i not in graph:
                    return False
                graph[i] -= 1
                if graph[i] == 0:
                    del graph[i]
                    heapq.heappop(minHeap)
        return True