class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = defaultdict(list)
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        
        cycle = set()
        visiting = set()
        out = []
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
            out.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return out