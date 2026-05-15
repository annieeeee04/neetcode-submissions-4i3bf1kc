class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle = set()
        visiting = set()
        path = []
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
            path.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return path