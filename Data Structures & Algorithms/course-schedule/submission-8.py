class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle = set()
        visiting = set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visiting:
                return True
            
            cycle.add(i)
            for preq in preqs[i]:
                if not dfs(preq): return False
            cycle.remove(i)
            visiting.add(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i): 
                return False
        return True
