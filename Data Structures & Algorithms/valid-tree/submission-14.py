class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        
        def dfs(node, prev):
            visited.add(node)
            for e in graph[node]:
                if e == prev:
                    continue
                if e in visited:
                    return False
                if not dfs(e, node):
                    return False

            return True
        
        return dfs(0,-1) and len(visited) == n
        
