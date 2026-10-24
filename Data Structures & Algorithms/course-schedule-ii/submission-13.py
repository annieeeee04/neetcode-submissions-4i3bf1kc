class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        visiting = set()
        path = []
        preqs = defaultdict(list)
        for crs, preq in prerequisites:
            preqs[crs].append(preq)

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
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return path
