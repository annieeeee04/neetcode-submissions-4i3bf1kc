class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            stack = []
            visited.add(node)
            stack.append((node, -1))

            while stack:
                cur, prev = stack.pop()
                for e in graph[cur]:
                    if e == prev:
                        continue
                    if e not in visited:
                        visited.add(e)
                        stack.append((e, cur))
        num = 0
        for node in range(n):
            if node not in visited:
                num += 1
                dfs(node)
        return num