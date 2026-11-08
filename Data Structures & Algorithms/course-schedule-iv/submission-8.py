class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preqs = defaultdict(list)
        for preq, crs in prerequisites:
            preqs[crs].append(preq)
        
        memo = {}
        def dfs(p, c):
            if (p,c) in memo:
                return memo[(p,c)]
            
            res = p in preqs[c] or any(dfs(p,q) for q in preqs[c])
            memo[(p,c)] = res
            return memo[(p,c)]
        
        return [dfs(u,v) for u,v in queries]