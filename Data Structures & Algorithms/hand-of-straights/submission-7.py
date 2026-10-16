class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        graph = {}

        for n in hand:
            graph[n] = graph.get(n,0) + 1
        
        minHeap = list(graph.keys())
        heapq.heapify(minHeap)

        while minHeap:
            cur = minHeap[0]
            for i in range(groupSize):
                if graph.get(cur+i,0) == 0:
                    return False
                graph[cur+i] -= 1
                if graph[cur+i] == 0:
                    heapq.heappop(minHeap)
        return True