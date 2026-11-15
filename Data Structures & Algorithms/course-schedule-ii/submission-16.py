class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nxtCrs = defaultdict(list)
        degree = [0] * numCourses
        for crs, pre in prerequisites:
            nxtCrs[pre].append(crs)
            degree[crs] += 1
        
        queue = deque(c for c in range(numCourses) if degree[c] == 0)
        out = []
        while queue:
            c = queue.popleft()
            out.append(c)

            for nb in nxtCrs[c]:
                degree[nb] -= 1
                if degree[nb] == 0:
                    queue.append(nb)
        return out if len(out) == numCourses else []