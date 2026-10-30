class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
        
        def bst(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            
            queue = deque([(src, 1.0)])
            visited = {src}
            while queue:
                node, prod = queue.popleft()
                if node == dst:
                    return prod
                
                for nb, w in graph[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append((nb, w * prod))
            return -1.0
        
        return [bst(u,v) for u,v in queries]