class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle = set()
        visiting = set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visiting:
                return True
            
            cycle.add(c)
            for p in preqs[c]:
                if not dfs(p): return False
            cycle.remove(c)
            visiting.add(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True