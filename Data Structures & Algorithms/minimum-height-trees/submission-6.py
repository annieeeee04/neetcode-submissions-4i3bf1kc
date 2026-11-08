class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        degree = [len(graph[i]) for i in range(n)]
        leaves = deque([e for e in range(n) if degree[e] == 1])
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