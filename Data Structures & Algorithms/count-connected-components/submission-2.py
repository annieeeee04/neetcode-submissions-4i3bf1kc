class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        graph = {i:[] for i in range(n)}
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        # go through all neighbors downstream the current node
        # and mark as visited
        def dfs(node):
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    dfs(neighbor)

        num = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                num += 1
        return num