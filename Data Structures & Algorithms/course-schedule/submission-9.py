class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        preqNum = [0] * numCourses

        for crs, preq in prerequisites:
            preqs[preq].append(crs)
            preqNum[crs] += 1
        
        queue = deque([c for c in range(numCourses) if preqNum[c] == 0])
        visited = 0
        while queue:
            p = queue.popleft()
            visited += 1
            for c in preqs[p]:
                preqNum[c] -= 1
                if preqNum[c] == 0:
                    queue.append(c)
        return visited == numCourses