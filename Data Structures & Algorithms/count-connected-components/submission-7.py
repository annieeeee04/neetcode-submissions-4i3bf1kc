class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        def bfs(node):
            queue = deque([node])
            visit.add(node)
            while queue:
                node = queue.popleft()
                for e in graph[node]:
                    if e not in visit:
                        queue.append(e)
                        visit.add(e)
        
        cnt = 0
        for i in range(n):
            if i not in visit:
                cnt += 1
                bfs(i)
        return cnt
