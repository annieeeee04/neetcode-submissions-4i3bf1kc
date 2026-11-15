class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a,b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
        
        memo = {}
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1
            
            queue = deque([(src, 1)])
            visited = {src}
            while queue:
                cur, prod = queue.popleft()
                if cur == dst:
                    return prod

                for nb, w in graph[cur]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append((nb, prod*w))
            return -1
        
        return [bfs(u,v) for u,v in queries]
                        