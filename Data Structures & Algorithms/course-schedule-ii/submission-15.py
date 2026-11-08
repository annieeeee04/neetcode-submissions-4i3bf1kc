class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nxt_courses = defaultdict(list)
        preqNum = [0] * numCourses
        for crs, preq in prerequisites:
            nxt_courses[preq].append(crs)
            preqNum[crs] += 1
        
        queue = deque([c for c in range(numCourses) if preqNum[c] == 0])

        out = []
        while queue:
            p = queue.popleft()
            out.append(p)

            for c in nxt_courses[p]:
                preqNum[c] -= 1
                if preqNum[c] == 0:
                    queue.append(c)

        return out if len(out) == numCourses else []