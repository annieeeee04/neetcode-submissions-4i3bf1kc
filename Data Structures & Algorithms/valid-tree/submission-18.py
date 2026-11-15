class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {0}
        q = deque([[0, -1]])

        while q:
            node, prev = q.popleft()
            for e in graph[node]:
                if e == prev:
                    continue
                if e in visited:
                    return False
                visited.add(e)
                q.append((e, node))
        return len(visited) == n