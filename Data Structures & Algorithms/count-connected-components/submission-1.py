# Time: O(N + E)
# Space: O(N + E)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        def dfs(node):
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor not in visit:
                    dfs(neighbor)

        cnt = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                cnt += 1
        return cnt