class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = len(hand)
        if m % groupSize != 0: return False

        graph = {}
        for n in hand:
            graph[n] = graph.get(n, 0) + 1
        
        minH = list(graph.keys())
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in graph:
                    return False
                graph[i] -= 1
                if graph[i] == 0:
                    del graph[i]
                    heapq.heappop(minH)
        return True