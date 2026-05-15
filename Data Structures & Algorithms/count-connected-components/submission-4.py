class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = []
        def dfs(node):
            stack.append(node)
            while stack:
                cur = stack.pop()
                for e in graph[cur]:
                    if e not in visited:
                        stack.append(e)
                        visited.add(e)
        cnt = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                cnt += 1
        return cnt
