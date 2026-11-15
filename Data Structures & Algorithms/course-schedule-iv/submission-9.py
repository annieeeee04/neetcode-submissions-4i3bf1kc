class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preqs = defaultdict(list)
        for pre, crs in prerequisites:
            preqs[crs].append(pre)
        
        memo = {}
        def dfs(u, v):
            if (u,v) in memo:
                return memo[(u,v)]
            
            res = u in preqs[v] or any(dfs(u,p) for p in preqs[v])
            memo[(u,v)] = res
            return memo[(u,v)]
        
        return [dfs(u,v) for u,v in queries]