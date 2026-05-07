class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for neighbor in graph[i]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n