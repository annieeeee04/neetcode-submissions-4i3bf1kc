class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
            
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for nb in graph[i]:
                if nb == prev:
                    continue
                if not dfs(nb, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n