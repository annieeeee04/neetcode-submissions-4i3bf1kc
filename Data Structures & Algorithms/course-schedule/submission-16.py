class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nxtCrs = defaultdict(list)
        preqNum = [0] * numCourses
        for crs, pre in prerequisites:
            nxtCrs[pre].append(crs)
            preqNum[crs] += 1
        
        queue = deque(c for c in range(numCourses) if preqNum[c] == 0)
        visited = 0
        while queue:
            c = queue.popleft()
            visited += 1
            for nxt in nxtCrs[c]:
                preqNum[nxt] -= 1
                if preqNum[nxt] == 0:
                    queue.append(nxt)
                    
        return visited == numCourses
        