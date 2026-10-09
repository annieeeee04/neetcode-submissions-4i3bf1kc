class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nexts = defaultdict(list)
        preqNum = [0] * numCourses
        for crs, preq in prerequisites:
            nexts[preq].append(crs)
            preqNum[crs] += 1
        
        out = []
        queue = deque()
        for c in range(numCourses):
            if preqNum[c] == 0:
                queue.append(c)
        
        while queue:
            c = queue.popleft()
            out.append(c)
            for nextCrs in nexts[c]:
                preqNum[nextCrs] -= 1
                if preqNum[nextCrs] == 0:
                    queue.append(nextCrs)
                    
        return out if len(out) == numCourses else []
