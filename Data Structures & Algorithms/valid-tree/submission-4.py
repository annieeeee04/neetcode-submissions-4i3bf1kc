class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        visit.add(0)
        q = deque([[0,-1]])
        
        while q:
            node, prev = q.popleft()
            for edg in graph[node]:
                if edg == prev:
                    continue
                if edg in visit:
                    return False
                visit.add(edg)
                q.append([edg, node])
        
        return len(visit) == n