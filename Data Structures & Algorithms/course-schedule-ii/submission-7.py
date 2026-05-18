class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        next_crs = defaultdict(list)
        preq_nums = [0] * numCourses
        for crs, preq in prerequisites:
            next_crs[preq].append(crs)
            preq_nums[crs] += 1
        
        queue = deque([c for c in range(numCourses) if preq_nums[c] == 0])
        path = []
        while queue:
            p = queue.popleft()
            path.append(p)

            for c in next_crs[p]:
                preq_nums[c] -= 1
                if preq_nums[c] == 0:
                    queue.append(c)
        
        return path if len(path) == numCourses else []