# BFS

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit = set()
        visit.add(0)
        q = deque([[0,-1]])

        while q:
            i, prev = q.popleft()
            for e in graph[i]:
                if e == prev:
                    continue
                if e in visit:
                    return False
                q.append((e,i))
                visit.add(e)
        
        return len(visit) == n