class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course: [preq]
        preqs = {i: [] for i in range(numCourses)} 
        for pre in prerequisites:
            preqs[pre[0]].append(pre[1])
        seen = set()

        def dfs(c):
            if c in seen:
                return False
            
            if preqs[c] == []:
                return True

            seen.add(c)
            for p in preqs[c]:
                if not dfs(p): return False
            seen.remove(c)
            preqs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
