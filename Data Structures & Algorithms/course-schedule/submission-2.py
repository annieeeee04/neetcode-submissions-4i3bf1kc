class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course: [preq]
        preqs = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        visiting = set()
        cycle = set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visiting:
                return True
            
            cycle.add(c)
            for preq in preqs[c]:
                if not dfs(preq):
                    return False
            cycle.remove(c)
            visiting.add(c)
            preqs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True