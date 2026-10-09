class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([(0, -1)])
        visited.add(0)
        while queue:
            node, prev = queue.popleft()
            for e in graph[node]:
                if e == prev:
                    continue
                if e in visited:
                    return False
                visited.add(e)
                queue.append([e, node])
        return len(visited) == n