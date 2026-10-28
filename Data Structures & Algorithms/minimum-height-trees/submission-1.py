# Time: O(n)
# Space: O(n)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        degrees = [len(nbs) for nbs in graph]
        leaves = deque(i for i in range(n) if degrees[i] == 1)
        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for nb in graph[leaf]:
                    degrees[nb] -= 1
                    if degrees[nb] == 1:
                        leaves.append(nb)

        return list(leaves)