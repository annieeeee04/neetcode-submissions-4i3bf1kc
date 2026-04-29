class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle = set()
        visiting = set()
        out = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visiting:
                return True
            
            cycle.add(c)
            for preq in preqs[c]:
                if not dfs(preq): return False
            cycle.remove(c)
            visiting.add(c)
            out.append(c)
            preqs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return out