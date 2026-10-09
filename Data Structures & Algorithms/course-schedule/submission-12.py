class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nexts = defaultdict(list)
        preqNum = [0] * numCourses
        for crs, prq in prerequisites:
            nexts[prq].append(crs)
            preqNum[crs] += 1
        
        q = deque()
        for c in range(numCourses):
            if preqNum[c] == 0:
                q.append(c)

        visited = 0
        while q:
            visited += 1
            p = q.popleft()
            for c in nexts[p]:
                preqNum[c] -= 1
                if preqNum[c] == 0:
                    q.append(c)
        return visited == numCourses