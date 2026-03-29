class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course: [preq]
        preqs = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle = set()
        visit = set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for p in preqs[c]:
                if not dfs(p): return False
            cycle.remove(c)
            visit.add(c)
            preqs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True