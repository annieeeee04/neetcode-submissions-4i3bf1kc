# Time: O(n + E), each node is pushed once, each edge looked at twice
# Space: O(n + E), adjacency list + visit + stack
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            stack = []
            stack.append(node)
            visited.add(node)
            while stack:
                cur = stack.pop()
                for nb in graph[cur]:
                    if nb not in visited:
                        stack.append(nb)
                        visited.add(nb)
        
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt