class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        preqNum = [0] * numCourses
        for crs, pre in prerequisites:
            preqs[pre].append(crs)
            preqNum[crs] += 1
        
        queue = deque()
        for n in range(numCourses):
            if preqNum[n] == 0:
                queue.append(n)
        
        visited = set()
        while queue:
            p = queue.popleft()
            visited.add(p)
            for c in preqs[p]:
                preqNum[c] -= 1
                if preqNum[c] == 0:
                    queue.append(c)
        
        return len(visited) == numCourses