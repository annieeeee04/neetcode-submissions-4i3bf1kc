class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for nb in graph[node]:
                if nb == prev:
                    continue
                if not dfs(nb, node): return False
            return True
        
        return dfs(0,-1) and len(visit) == n