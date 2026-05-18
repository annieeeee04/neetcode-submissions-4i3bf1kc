class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        visited.add(0)
        stack = [(0, -1)] # node, prev
        while stack:
            cur, prev = stack.pop()
            
            for e in graph[cur]:
                if e == prev:
                    continue
                elif e in visited:
                    return False
                
                visited.add(e)
                stack.append((e, cur))
        return len(visited) == n