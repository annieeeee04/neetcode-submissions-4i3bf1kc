class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        out = []
        visiting = set()
        cycle = set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visiting: 
                return True
                
            cycle.add(c)
            for p in preqs[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visiting.add(c)
            out.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return out