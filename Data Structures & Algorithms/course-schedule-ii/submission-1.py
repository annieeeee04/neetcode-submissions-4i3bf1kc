class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle, visit = set(), set()
        out = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for preq in preqs[c]:
                if not dfs(preq): return False
            cycle.remove(c)
            visit.add(c)
            preqs[c] = []
            out.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return out