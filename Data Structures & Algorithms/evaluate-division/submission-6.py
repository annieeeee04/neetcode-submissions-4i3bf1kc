class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a,b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1
               
            queue = deque([(src, 1.0)])
            visited = {src}
            while queue:
                node, prod = queue.popleft()
                if node == dst:
                    return prod
                for nxt, w in graph[node]:
                    if nxt not in visited:
                        queue.append((nxt, prod*w))
                        visited.add(nxt)
            return -1
        return [bfs(u,v) for u,v in queries]