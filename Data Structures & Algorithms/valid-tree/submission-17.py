class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        queue = deque()
        queue.append((0,-1))
        visited.add(0)
        while queue:
            cur, prev = queue.popleft()
            
            for nb in graph[cur]:
                if nb == prev:
                    continue
                if nb in visited:
                    return False
                queue.append((nb, cur))
                visited.add(nb)
        return True if len(visited) == n else False