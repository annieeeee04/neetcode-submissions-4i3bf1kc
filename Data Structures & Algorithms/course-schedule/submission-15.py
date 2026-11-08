class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_crs = defaultdict(list)
        preqNum = [0] * numCourses
        for crs, preq in prerequisites:
            next_crs[preq].append(crs)
            preqNum[crs] += 1
        
        q = deque([c for c in range(numCourses) if preqNum[c] == 0])
        seen = 0
        while q:
            size = len(q)
            for _ in range(size):
                c = q.popleft()
                seen += 1
                for nxt in next_crs[c]:
                    preqNum[nxt] -= 1
                    if preqNum[nxt] == 0:
                        q.append(nxt)
        return seen == numCourses
        
        