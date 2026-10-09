class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque()
        queue.append([0,-1])
        visit = set()
        visit.add(0)

        while queue:
            cur, prev = queue.popleft()
            for nb in graph[cur]:
                if nb == prev:
                    continue
                if nb in visit:
                    return False
                visit.add(nb)
                queue.append([nb, cur])
        
        return len(visit) == n