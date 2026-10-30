class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return list(range(n))
        
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        degree = [len(nbs) for nbs in graph]
        leaves = deque(i for i in range(n) if degree[i] == 1)
        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size
            for _ in range(size):
                leaf = leaves.popleft()
                for nb in graph[leaf]:
                    degree[nb] -= 1
                    if degree[nb] == 1:
                        leaves.append(nb)
        return list(leaves)