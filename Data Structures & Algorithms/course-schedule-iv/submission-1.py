class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preqs = defaultdict(list)
        for preq, crs in prerequisites:
            preqs[crs].append(preq)
        
        out = [False] * len(queries)
        cache = {}
        def dfs(u, v):
            if (u,v) in cache:
                return cache[(u,v)]
            res = u in preqs[v] or any(dfs(u,p) for p in preqs[v])
            cache[(u,v)] = res
            return cache[(u,v)]

        return [dfs(u, v) for u, v in queries]